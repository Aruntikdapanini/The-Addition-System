import streamlit as st

# Setup the page styling
st.set_page_config(page_title="THE + system", page_icon="🧊", layout="centered")
st.title("THE Addition System")
st.write("Select two ppl to perform addition")

# Your data engine list
listrel = [["ciaoale", 18, 18, 5, 5, 46, 60], ["rojorockwell", 20, 20, 5, 4, 49, 50], ["aruntik", 18, 17, 5, 4, 44, 75], ["loi", 16, 16, 4, 5, 41, 70], ["java", 17, 13, 5, 5, 40, 30], ["neket", 18, 16, 5, 3, 42, 50], ["oeis", 17, 14, 5, 5, 41, 15], ["light", 11, 11, 3, 3, 28, 15], ["shadow", 16, 14, 1, 1, 32, 35], ["cat", 13, 7, 3, 4, 27, 35], ["vben1", 16, 13, 4, 4, 37, 55], ["fabian", 11, 10, 3, 3, 27, 25], ["tim", 2, 11, 2, 2, 17, 30], ["eden", 11, 11, 3, 3, 28, 25], ["jovaa", 6, 7, 3, 3, 19, 0], ["pioter", 7, 6, 2, 5, 20, 45], ["iexm", 11, 10, 1, 1, 23, 15], ["gorfe", 10, 6, 1, 4, 21, 10], ["enlgish", 7, 9, 0, 2, 18, 5], ["ray", 20, 19, 5, 4, 48, 90], ["shahir", 18, 17, 3, 4, 42, 35], ["3ha6", 14, 13, 2, 1, 30, 45], ["landy", 17, 17, 4, 3, 41, 50], ["weenie", 19, 17, 5, 3, 44, 80], ["rankkuri", 16, 15, 3, 1, 35, 50], ["olego", 19, 18, 5, 3, 45, 70], ["amber", 17, 17, 4, 0, 38, 35], ["carolyn", 18, 16, 5, 5, 44, 35], ["snur", 11, 14, 2, 2, 29, 40], ["fini", 15, 17, 5, 5, 42, 50], ["night", 14, 12, 2, 4, 32, 40], ["normallyy", 7, 13, 3, 4, 27, 15], ["lennerd", 15, 17, 5, 2, 39, 15], ["shuhzhu", 17, 17, 4, 3, 41, 55], ["nomi", 14, 7, 3, 3, 27, 30], ["emi", 17, 17, 5, 4, 43, 100], ["em24", 13, 14, 4, 3, 34, 15], ["itzmez0", 13, 13, 3, 2, 31, 40], ["arch", 3, 2, 2, 2, 9, 30], ["eg430", 5, 7, 2, 0, 14, 15], ["stzu", 14, 14, 2, 2, 32, 35], ["lilmommasboy", 14, 14, 2, 2, 32, 45], ["hayden", 11, 14, 2, 5, 32, 40], ["hdog", 5, 8, 1, 2, 16, 50], ["icy", 6, 13, 2, 1, 22, 10], ["kritzr", 14, 14, 2, 2, 32, 35], [".spooky", 17, 16, 4, 3, 40, 50], ["babagameZ", 14, 10, 2, 2, 28, 40], ["superN57", 14, 16, 5, 3, 38, 20], ["Tae", 17, 17, 4, 2, 40, 55], ["3bc", 9, 6, 2, 3, 20, 15], ["bailey", 3, 10, 4, 1, 18, 25], ["ducksit", 14, 13, 4, 3, 34, 30], ["error", 11, 13, 4, 4, 32, 35], ["frankie", 16, 14, 2, 3, 35, 85], ["amphier", 15, 14, 3, 5, 37, 45], ["glaciers", 10, 11, 2, 5, 28, 40], [".cinnamon", 16, 16, 2, 1, 35, 35], ["minty", 14, 13, 2, 1, 30, 45], ["szam", 15, 16, 4, 3, 38, 50], ["tenken", 16, 17, 3, 3, 39, 60], ["break", 19, 18, 5, 5, 47, 50], ["bomo", 10, 14, 3, 2, 29, 20], ["blucky", 9, 14, 4, 2, 29, 35], ["anto", 14, 13, 3, 2, 32, 40], ["sandoony", 2, 5, 2, 1, 10, 10]]

# Extract profile names automatically into a list for dropdown selectors
profile_names = []
idx = 0
while idx < len(listrel):
    profile_names.append(listrel[idx][0])
    idx += 1

# Create the webpage layout with side-by-side dropdown lists
col1, col2 = st.columns(2)
with col1:
    selection_a = st.selectbox("Choose Person A", profile_names, index=0)
with col2:
    selection_b = st.selectbox("Choose Person B", profile_names, index=1)

if st.button("^^Additioner^^", use_container_width=True):
    a = selection_a
    b = selection_b
    i = 0
    sumrel = []
    while i < len(listrel):
        if listrel[i][0] == a:
            a = i
        if listrel[i][0] == b:
            b = i
        i += 1
    i = 0
    while i < len(listrel[0])-1:
        if i == 0:
            ae = str(listrel[a][0] + " + " + listrel[b][0])
            sumrel.append(ae)
        i += 1
        temprel = round((listrel[a][i] + listrel[b][i])/2)
        sumrel.append(temprel)
    i = 0
    listrelbutSI = []
    while i < len(listrel):
        SI = 4*(abs(sumrel[3] - listrel[i][3]) + abs(sumrel[4] - listrel[i][4])) + 5*((abs(sumrel[1] - listrel[i][1])) + abs(sumrel[2] - listrel[i][2])) + 3*abs(sumrel[5] - listrel[i][5]) + 0.5*abs(sumrel[6]-listrel[i][6])
        listrelbutSI.append(SI)
        i += 1
    listrelbutcopy = sorted(listrelbutSI)
    listrelbuttop = []
    top_count = 0 
    i = 0
    while i < len(listrel) and top_count < 5:
        if listrelbutSI[i] == listrelbutcopy[top_count]:
            if [listrel[i][0], listrelbutSI[i]] not in listrelbuttop:
                listrelbuttop.append([listrel[i][0], listrelbutSI[i]])
                top_count += 1 
                i = -1 # Triggers a clean loop restart from 0 next turn
        i += 1 

    # Emergency safety net while loop so identical profiles never throw index errors
    while len(listrelbuttop) < 5:
        listrelbuttop.append(listrelbuttop[-1])

    # --- Modern Web Presentation UI ---
    st.markdown(f"### 🧊 `{listrel[a][0]}` + `{listrel[b][0]}` Best Matches 🧊")
    
    # Beautiful visual dashboard cards using Streamlit metrics
    st.metric(label="🥇 Top 1 Best Match", value=listrelbuttop[0][0], delta=f"{100 - listrelbuttop[0][1]}% Score")
    
    col_left, col_right = st.columns(2)
    with col_left:
        st.write(f"🥈 **Top 2:** {listrelbuttop[1][0]} (`{100 - listrelbuttop[1][1]}%`)")
        st.write(f"🥉 **Top 3:** {listrelbuttop[2][0]} (`{100 - listrelbuttop[2][1]}%`)")
    with col_right:
        st.write(f"🏅 **Top 4:** {listrelbuttop[3][0]} (`{100 - listrelbuttop[3][1]}%`)")
        st.write(f"🧊 **Top 5:** {listrelbuttop[4][0]} (`{100 - listrelbuttop[4][1]}%`)")