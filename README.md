# powerlifting-calculator
 
Name - Shivesh Jha
Reg. No. - 25BAI10748
 
📘 README FILE (GitHub)
🏋️ Powerlifting Load Calculator

A simple and intelligent tool that helps powerlifters select the right training weight using RPE-based calculations and structured programming.

🚀 Features
Estimate 1RM from any set
Suggest next weight based on target RPE
Manual mode for full control
Built-in 5/3/1 program support
Realistic rounding (2.5 kg / 5 kg)
Clean Streamlit interface
🧠 How It Works

The app uses:

RPE → Reps in Reserve (RIR) conversion
Effective reps calculation
1RM estimation formula

It then reverses the calculation to suggest the correct weight for the next set.

🛠️ Tech Stack
Python
Streamlit
Basic mathematical modeling
⚙️ Installation
Clone the repository:
git clone https://github.com/your-username/powerlifting-calculator.git
cd powerlifting-calculator
Install dependencies:
pip install streamlit
▶️ Running the App
streamlit run app.py
📋 Usage
Manual Mode:
Enter current set:
Weight
Reps
RPE
Enter target:
Reps
RPE
Select rounding
Click Calculate
5/3/1 Mode:
Enter current set
Select:
Mesocycle (1–4)
Set type (5x5 / 3x3 / 1x1)
Click Calculate

The app automatically determines target intensity.

📌 Example

Input:

100 kg × 5 @ RPE 7
Target: 5 reps @ RPE 8

Output:

Suggested weight ≈ 105 kg
📈 Future Improvements
Progress tracking with graphs
Video-based RPE estimation
Personalized recommendations
🤝 Contributing

Feel free to fork the repo and improve the project.

📄 License

This project is for academic purposes.

🙌 Acknowledgements

Inspired by strength training methodologies and RPE-based programming.
