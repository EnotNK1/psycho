import uuid

from database.database import database_service
from database.test_info import Test_maslach, Test_DASS

database_service.create_inquirty()
database_service.create_type_analysis()
database_service.create_test(Test_maslach)
print("1")
database_service.create_test(Test_DASS)
database_service.register_user(uuid.uuid4(), "admin", "admin", "admin", "", True, True, "", "", 0, True)