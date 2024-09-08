import uuid

from database.services.teest import database_service
from database.test_info import Test_maslach, Test_DASS, Test_STAI, Test_coling_strategy, Test_cmq, Test_jas, Test_bek21
from database.edu_info import Base, Cbt_base, Burnout, Breathing_techniques, Relaxation_techniques, Coping_strategies

database_service.create_inquirty()
database_service.create_type_analysis()
database_service.create_test(Test_maslach)
database_service.create_test(Test_DASS)
database_service.create_test(Test_STAI)
database_service.create_test(Test_coling_strategy)
database_service.create_test(Test_cmq)
database_service.create_test(Test_jas)
database_service.create_test(Test_bek21)
database_service.create_education(Base)
database_service.create_education(Cbt_base)
database_service.create_education(Burnout)
database_service.create_education(Breathing_techniques)
database_service.create_education(Relaxation_techniques)
database_service.create_education(Coping_strategies)
database_service.register_user(uuid.uuid4(), "admin", "admin", "admin", "", True, True, "", "", 0, True)