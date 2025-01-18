from core.authentication.models import GuildMemberData, Student

def update_member_data(action, office, student_id):
    student = Student.objects.get(id=student_id)
    
    if action == 'create':
        create()
    elif action == 'delete':
        delete()
    else:
        raise ValueError("Ação inválida. Use 'create' ou 'delete'.")
    
    def create ():
        """
        Cria um registro de GuildMemberData para o estudante
        
        Args:
        action (str): Ação a ser realizada
        office (str): Office para o qual será associado o estudante
        student (int): Estudante para o qual será criado um registro
        
        """
        GuildMemberData.objects.create(student=student, office=office)
    def delete ():
        """
        Deleta todos os registros de GuildMemberData para o estudante
        
        Args:
        student (int): Estudante para o qual será deletado um registro
        
        """
        GuildMemberData.objects.filter(student=student).delete()
    
        
        