"""Create, read, update, and delete operations"""

# importing tables for database 
from model import db, Owner, Dog, Meal, Mood, Activity, Training, Grooming, Note, connect_to_db

# -------------------------------------- #

"""CREATE FUNCTIONS"""

# Create a new owner
def create_owner(email,first_name, last_name, password):
    owner = Owner(email=email, first_name=first_name, last_name=last_name, password=password)
    db.session.add(owner)
    db.session.commit()
    return owner

# Create a new dog
def create_dog(owner_email, dog_name, dog_bio, dog_img):
    dog = Dog(owner_email=owner_email, dog_name=dog_name, dog_bio=dog_bio, dog_img=dog_img)
    db.session.add(dog)
    db.session.commit()
    return dog

# Create a new meal
def create_meal(dog_id, meal_type, meal_date, meal_time):
    meal = Meal(dog_id=dog_id, meal_type=meal_type, meal_date=meal_date, meal_time=meal_time)
    db.session.add(meal)
    db.session.commit()
    return meal

# Create a new mood
def create_mood(dog_id, mood_type, mood_date, mood_note):
    mood = Mood(dog_id=dog_id, mood_type=meal_type, mood_date=meal_date, mood_note=mood_note)
    db.session.add(mood)
    db.session.commit()
    return mood

# Create new activity
def create_activity(dog_id, activity_type, activity_date, activity_time, activity_duration, activity_note):
    activity = Activity(dog_id=dog_id,activity_type=activity_type, activity_date=activity_date, activity_time=activity_time, activity_duration=activity_duration, activity_note=activity_note)
    db.session.add(activity)
    db.session.commit()
    return activity

# Create new training
def create_training(dog_id, training_type, training_date, training_time, training_duration, training_note):
    training = Training(dog_id=dog_id, training_type=training_type, training_date=training_date, training_time=training_time, training_duration=training_duration, training_note=training_note)
    db.session.add(training)
    db.session.commit()
    return training

# Create new grooming
def create_grooming(dog_id, grooming_type, grooming_date):
    grooming = Grooming(dog_id=dog_id, grooming_type=grooming_type, grooming_date=grooming_date)
    db.session.add(grooming)
    db.session.commit()
    return grooming

# Create new note
def create_note(dog_id, note_date, note):
    note = Note(dog_id=dog_id, note_date=note_date, note=note)
    db.session.add(note)
    db.session.commit()
    return note

# -------------------------------------- #

"""READ/GET FUNCTIONS"""

# Get a user by email address at log in
def get_owner_by_email(email):
    return Owner.query.filter_by(email=email).first()

# Get all meals by date and dog_id
def get_all_meals(dog_id, date):
    return Meal.query.filter((Meal.dog_id == dog_id) & (Meal.meal_date == date))
# Get all moods by date and dog_id
# Get all activities by date and dog_id
# Get all training sessions by date and dog_id
# Get all grooming sessions by date and dog_id
# Get all notes by date and dog_id

# -------------------------------------- #

"""CONNECTING TO SERVER AND CREATING TABLES"""

if __name__ == '__main__':
    from server import app
    connect_to_db(app)