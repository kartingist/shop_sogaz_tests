BirthdayValidate=[
                  (17, 'male'),
                  (18, 'male'),
                  (64, 'male'),
                  (65, 'male'),
                  (17, 'famale'),
                  (18, 'famale'),
                  (59, 'famale'),
                  (60, 'famale')
                 ]

CyrillicValidate_negative=[
                    ("test", "11"),
                    ("теst", "aA"),
                    ("тест test", "фФ"),
                    ("тест.", ".!"),
                    ("тест@", "№;%"),
                    ("тест123", "?*()")
                 ]
CyrillicValidate_positive=[
                    ("тест"),
                    ("тест-тест"),
                    ("тест тест"),
                    ("тест'"),
                    ("ТЕСТ")
                 ]
CyrillicAndNumberValidate= [
                    ("тест 123"),
                    ("тест."),
                    ("тест'"),
                    ("тест_"),
                    ("ТЕСТ")
                 ]

PersonalCodeValidate=["", "1", "333", "4444", "88888888", "999999999"]


DateStartPassNegValidate=[
                        (14, -1 ),
                        (20, -1 ),
                        (45, -1 ),
                        (20, 370 ),
                        (0, 5400 ),
                     ]

DateStartPassPosValidate=[
                        (20, 0),
                        (20, 31 ),
                        (45, 0),
                        (45, 31),
                     ]
# DivisionValidate;
# EmailValidate;
# PassValidate;
# PhoneValidate;