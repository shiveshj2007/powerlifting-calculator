import streamlit as st


#Calculating Functions

def estimate_1rm(weight, reps, rpe):
    rir = 10 - rpe
    r_eff = reps + rir
    return weight * (1 + (r_eff / 30))


def suggest_weight(current_weight, current_reps, current_rpe, target_reps, target_rpe):
    onerm = estimate_1rm(current_weight, current_reps, current_rpe)
    target_rir = 10 - target_rpe
    target_r_eff = target_reps + target_rir
    return onerm / (1 + (target_r_eff / 30))


def round_weight(weight, base):
    ratio = weight / base
    rounded = round(ratio) * base
    return round(rounded, 1)


#Program Data

program = {
    1: {"5x5": 6.5, "3x3": 7, "1x1": 8},
    2: {"5x5": 7.5, "3x3": 8, "1x1": 8.5},
    3: {"5x5": 8, "3x3": 8.5, "1x1": 9.5},
    4: {"5x5": 8.5, "3x3": 9.5, "1x1": 10}
}


#UI

st.title("🏋️ Powerlifting Load Calculator")

mode = st.selectbox("Select Mode", ["Manual", "5/3/1"])

st.subheader("Current Set")
current_weight = st.number_input("Weight (kg)", min_value=0.0, step=2.5)
current_reps = st.number_input("Reps", min_value=1, step=1)
current_rpe = st.number_input("RPE", min_value=1.0, max_value=10.0, step=0.5)


#Choosing a mode

if mode == "Manual":
    st.subheader("Target Set")

    target_reps = st.number_input("Target Reps", min_value=1, step=1)
    target_rpe = st.number_input("Target RPE", min_value=1.0, max_value=10.0, step=0.5)

elif mode == "5/3/1":
    st.subheader("Program Selection")

    mesocycle = st.selectbox("Mesocycle", [1, 2, 3, 4])
    set_type = st.selectbox("Set Type", ["5x5", "3x3", "1x1"])

    target_reps = int(set_type.split("x")[0])
    target_rpe = program[mesocycle][set_type]

    st.write(f"Target: {target_reps} reps @ RPE {target_rpe}")

#Rounding weight

rounding = st.selectbox("Round to", [2.5, 5.0])

#Calculating

if st.button("Calculate Next Weight"):
    suggested = suggest_weight(
        current_weight,
        current_reps,
        current_rpe,
        target_reps,
        target_rpe
    )

    final_weight = round_weight(suggested, rounding)

    st.success(f"Suggested Weight: {final_weight} kg")