from vet_site.course_info.models import InfoSetting
from vet_site import settings 

def common(request):
    LC_TELEPHONE = InfoSetting.objects.get(key="LUCY_CAV_TELEPHONE").value
    TECHNICAL_SUPPORT = InfoSetting.objects.get(key="TECHNICAL_SUPPORT").value
    MEDIA_URL = settings.MEDIA_URL
    return locals()