from django.contrib import admin

from .models.applied_jobs import AppliedJob
from .models.city import City
from .models.company import Company
from .models.industry import Industry
from .models.job import Job
from .models.profession import Profession
from .models.profile import Profile
from .models.province import Province
from .models.skill import Skill
from .models.watchlist import Watchlist


admin.site.register(AppliedJob)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Industry)
admin.site.register(Job)
admin.site.register(Profession)
admin.site.register(Profile)
admin.site.register(Province)
admin.site.register(Skill)
admin.site.register(Watchlist)