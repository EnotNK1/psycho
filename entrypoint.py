import uuid

from database.services.create import create_service_db
from database.services.users import user_service_db
from database.test_info import Test_maslach, Test_DASS, Test_STAI, Test_coling_strategy, Test_cmq, Test_jas, Test_bek21
from database.edu_info import Base, Cbt_base, Burnout, Breathing_techniques, Relaxation_techniques, Coping_strategies

user_service_db.create_tables()
create_service_db.create_inquirty()
create_service_db.create_type_analysis()
create_service_db.create_test(Test_maslach)
create_service_db.create_test(Test_DASS)
create_service_db.create_test(Test_STAI)
create_service_db.create_test(Test_coling_strategy)
create_service_db.create_test(Test_cmq)
create_service_db.create_test(Test_jas)
create_service_db.create_test(Test_bek21)
create_service_db.create_education(Base)
create_service_db.create_education(Cbt_base)
create_service_db.create_education(Burnout)
create_service_db.create_education(Breathing_techniques)
create_service_db.create_education(Relaxation_techniques)
create_service_db.create_education(Coping_strategies)
user_service_db.register_user(uuid.uuid4(), "admin", "admin", "admin", "", True, True, "", "", 0, True)