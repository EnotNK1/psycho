import uuid

from database.database import database_service
from database.test_info import Test_maslach, Test_DASS, Test_STAI, Test_coling_strategy, Test_cmq, Test_jas, Test_bek21

database_service.create_inquirty()
database_service.create_type_analysis()
database_service.create_test(Test_maslach)
database_service.create_test(Test_DASS)
database_service.create_test(Test_STAI)
database_service.create_test(Test_coling_strategy)
database_service.create_test(Test_cmq)
database_service.create_test(Test_jas)
database_service.create_test(Test_bek21)
database_service.register_user(uuid.uuid4(), "admin", "admin", "admin", "", True, True, "", "", 0, True)