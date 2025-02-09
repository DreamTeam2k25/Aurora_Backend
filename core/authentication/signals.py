from django.db.models.signals import post_save
from django.urls import reverse
from django.dispatch import receiver
from core.authentication.models import GuildMemberData, Student
import uuid


@receiver(post_save, sender=GuildMemberData)
def guild_verification(sender, instance, created, **kwargs):
    if created:
        member_data = GuildMemberData.objects.get(id=instance.id).student
        member = Student.objects.get(id=member_data.id)
        
        print(member)

        token = str(uuid.uuid4())
        instance.verification_token = token
        instance.save()
    
        verify_url = reverse('verify', kwargs={'verify_token': token})
        
        try:
            print(verify_url)
        except Exception as e: 
            print("Erro ao enviar email de verificação:", str(e)) 