import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SYKO BOOSTER", layout="wide")

# تأكد من أن رابط databaseURL مطابق لصورتك
firebase_js = """
<script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/8.10.0/firebase-database.js"></script>
<script>
  const firebaseConfig = {
    apiKey: "AIzaSyAbrrwnTAYVa-z83G9plOfieP4bm1rxDtA",
    authDomain: "syko-booster.firebaseapp.com",
    projectId: "syko-booster",
    storageBucket: "syko-booster.firebasestorage.app",
    messagingSenderId: "53373305140",
    appId: "1:53373305140:web:0b69db40be835905206561",
    databaseURL: "https://syko-booster-default-rtdb.firebaseio.com"
  };
  firebase.initializeApp(firebaseConfig);
  const db = firebase.database();

  function login() {
    const user = document.getElementById('user-input').value.trim().toLowerCase();
    if(user.length < 3) { alert("أدخل يوزر صحيح"); return; }
    
    // محاولة الاتصال بقاعدة البيانات
    db.ref('users/' + user).once('value').then((snapshot) => {
      // إذا نجح الاتصال، سينقلك للصفحة التالية
      document.getElementById('login-box').style.display = 'none';
      document.getElementById('main-content').style.display = 'block';
      if(!snapshot.exists()) {
        db.ref('users/' + user).set({coins: 0});
      }
    }).catch((error) => {
      alert("خطأ في الاتصال بقاعدة البيانات: " + error.message);
    });
  }
</script>
"""

# تصميم الواجهة (CSS)
ui_html = """
<div id="login-box" style="text-align:center; padding:50px; color:white; font-family:sans-serif;">
  <h1 style="color:#0ff;">SYKO SYSTEM</h1>
  <input type="text" id="user-input" placeholder="INSTAGRAM USER" style="padding:10px; width:80%;">
  <button onclick="login()" style="padding:10px 20px; margin-top:20px; background:#0ff; border:none; cursor:pointer;">START</button>
</div>

<div id="main-content" style="display:none; text-align:center; color:white; font-family:sans-serif;">
  <h1 style="color:#ffd700;">WELCOME TO SYKO WORLD</h1>
  <p>جمع الكوينز الآن!</p>
</div>
"""

components.html(firebase_js + ui_html, height=600)
