import streamlit as st

def main():
    st.title("Hinza Dilawar Simple Calculator")

    # Define unique keys for widgets in the main function
    num1_key = "num1"
    num2_key = "num2"

    # Input numbers with unique keys
    num1 = st.number_input("Enter the first number", key=num1_key, step=0.1, format="%.2f")
    num2 = st.number_input("Enter the second number", key=num2_key, step=0.1, format="%.2f")

    # Select operation
    operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Calculate result
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            st.error("Error: Division by zero is not allowed.")
            return
        result = num1 / num2

    # Display result
    st.write(f"The result is: {result:.2f}")

    # Ask if the user wants to perform another calculation
    continue_calculation = st.radio("Do you want to perform another calculation?", ("Yes", "No"))

    if continue_calculation == "No":
        st.write("Goodbye!")

if __name__ == "__main__":
    main()