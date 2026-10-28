import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="VoltAge AI | Defect Scanner", layout="wide")

st.sidebar.title("VoltAge Energy Systems")
st.sidebar.markdown("### Edge-AI Quality Assurance")
st.sidebar.success("📸 Optical Sensor: ONLINE")
st.sidebar.success("🧠 Physics Engine: ACTIVE")
st.sidebar.success("⚙️ Conveyor PLC: SYNCED")

st.title("Micro-Weld Optical Inspection & Thermal Twin")
st.markdown("Intercepting Processes 5-9: Visual scanning and predictive Joule-heating analysis.")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### Process A: Live Optical Feed")
    # For the prototype, we use an uploaded image to simulate the industrial camera feed
    uploaded_file = st.file_uploader("Upload Weld Image for Inspection (Simulating 4K Feed)", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file is not None:
        # Read the image
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        st.image(image, caption="Raw Optical Feed", use_column_width=True)
        
        # --- COMPUTER VISION ALGORITHM (OpenCV) ---
        # Convert to grayscale
        gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        # Apply blur and edge detection (simulating finding the weld boundary)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        
        st.markdown("### Computer Vision: Edge Detection")
        st.image(edges, caption="OpenCV Defect Isolation", use_column_width=True, clamp=True)
        
        # Simulate calculating the pixel area of the weld
        # For prototype purposes, we simulate a random defect calculation
        simulated_weld_area = np.random.uniform(70.0, 100.0) # 100% is perfect
        
with col2:
    if uploaded_file is not None:
        st.markdown("### Process B: Joule-Heating Thermal Prediction")
        
        st.metric(label="Calculated Weld Surface Area", value=f"{simulated_weld_area:.1f}%", delta=f"{simulated_weld_area - 100:.1f}% from spec")
        
        # --- PHYSICS SIMULATION ---
        # If weld area is lower, resistance is higher, heat generation is exponential
        base_temp = 35.0
        resistance_multiplier = (100.0 / simulated_weld_area) ** 2
        predicted_temp = base_temp * resistance_multiplier
        
        st.markdown("#### Simulated 40-Amp High-Load Test (Process 9 Intercept)")
        
        if predicted_temp > 65.0:
            st.error(f"⚠️ PREDICTED THERMAL RUNAWAY: {predicted_temp:.1f} °C")
            st.markdown("### Process C: Automated Action")
            st.error("🚨 CONVEYOR BELT HALTED. ROUTING TO REWORK (Bypassing Step 7 & 8).")
            st.progress(100)
        elif predicted_temp > 50.0:
            st.warning(f"⚠️ MARGINAL HEAT DETECTED: {predicted_temp:.1f} °C")
            st.markdown("### Process D: BMS Calibration")
            st.warning("⚡ FLASHING BMS: Throttling max current draw for this specific cell block to 30 Amps.")
        else:
            st.success(f"✅ THERMAL PROFILE SAFE: {predicted_temp:.1f} °C")
            st.success("🟢 PACK APPROVED. CONVEYOR MOVING TO STEP 7.")
    else:
        st.info("Upload an image of a weld (or any circle/metallic object) to run the AI Computer Vision sequence.")
