# Gym workout Tracker---

workouts=[]

print("Welcome to workout Tracker ")

def add_workout():
    exercise=input("Exercise name ")
    sets=int(input("How many set you done today "))    
    reps_list=[]
    for i in range(1,sets+1):
        reps=int(input(f"How many reps in sets {i} "))
        reps_list.append(reps)

    weight=float(input("How much weight (kg) "))


    workout={
        "exercise":exercise,
        "sets":sets,
        "reps":reps_list,
        "weight":weight
    }

    workouts.append(workout)
    print("Workout added sucessfully !")

def view_workout():
        if not workouts:
            print("No record yet!")
        else:
            for index,w in enumerate(workouts,start=1):
                print(f"{index}.{w['exercise']} | {w['sets']} sets | {w['reps']} reps | {w['weight']} kg")

def total_workout():
        if not workouts:
            print("No workout done today!")
        else:
            print(f"Total exercise you done today {len(workouts)}")
while True :
        print("1. Add Workout")
        print("2. View Workout")
        print("3. Total Workout")
        print("4. Exit")
        choice=int(input('Enter your choice'))
        if choice==1:
            add_workout()
        elif choice==2:
            view_workout()
        elif choice==3:
            total_workout()
        elif choice==4:
            print("Thanx for access the workout tracker")
            break
        else:
            print("Invalid Choice !")

            





