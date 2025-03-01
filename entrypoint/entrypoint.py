import uuid

from database.services.create import create_service_db
from database.services.users import user_service_db
from database.test_info import Test_maslach, Test_DASS, Test_STAI, Test_coling_strategy, Test_cmq, Test_jas, Test_bek21, Test_stress
from database.edu_info import Cbt_base, Burnout, Breathing_techniques, Relaxation_techniques, Coping_strategies, \
    Beliefs, Cbt_diary
from database.exercise_info import Cpt_diary, Definition_group_problems, Definition_problems_setting_goals, \
    Problem_analysis, Testing_beliefs, Beliefs_analysis, Mood_tracker, Note
from database.services.daily_task import daily_task_service_db
import time

create_service_db.create_inquirty()
create_service_db.create_type_analysis()
create_service_db.create_test(Test_maslach)
create_service_db.create_test(Test_DASS)
create_service_db.create_test(Test_STAI)
create_service_db.create_test(Test_coling_strategy)
create_service_db.create_test(Test_cmq)
create_service_db.create_test(Test_jas)
create_service_db.create_test(Test_bek21)
create_service_db.create_test(Test_stress)
# create_service_db.create_education(Base)
create_service_db.create_education(Cbt_base)
create_service_db.create_education(Burnout)
create_service_db.create_education(Breathing_techniques)
create_service_db.create_education(Relaxation_techniques)
create_service_db.create_education(Coping_strategies)
create_service_db.create_education(Beliefs)
create_service_db.create_education(Cbt_diary)

first_ex = create_service_db.create_exercise_structure(Cpt_diary, None)
second_ex = create_service_db.create_exercise_structure(Definition_group_problems, first_ex)
third_ex = create_service_db.create_exercise_structure(Definition_problems_setting_goals, second_ex)
fourth_ex = create_service_db.create_exercise_structure(Problem_analysis, third_ex)
fifth_ex = create_service_db.create_exercise_structure(Testing_beliefs, fourth_ex)
sixth_ex = create_service_db.create_exercise_structure(Beliefs_analysis, fifth_ex)
fourth_ex = create_service_db.create_exercise_structure(Mood_tracker, sixth_ex)
eighth_ex = create_service_db.create_exercise_structure(Note, fourth_ex)

create_service_db.get_destination_id_for_daily_task()
create_service_db.create_daily_task()