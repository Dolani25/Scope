
    
    //populate the app with cryptoairdrops with api
      function $(query) {

    return document.querySelector(query)

}

function $$(query) {

    return document.querySelectorAll(query)

}

//GOOGLE ACCOUNT onSignIn
function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  alert('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  alert('Name: ' + profile.getName());
  alert('Image URL: ' + profile.getImageUrl());
  alert('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
}



        // Function to update notification count
        function updateNotificationCount(count) {
            const countElement = document.querySelector('.notification-count');
            countElement.textContent = count > 0 ? count : '';
        }

        // Example usage:
        // updateNotificationCount(3); // Sets count to 3
        // updateNotificationCount(0); // Hides the count
     
     /* deals with Airdrop or Token ratings*/
        document.addEventListener('DOMContentLoaded', () => {
            const progressBars = document.querySelectorAll('.circular-progress');
            
            progressBars.forEach(bar => {
                const rating = parseFloat(bar.dataset.rating);
                const progress = (rating / 5) * 100; // Convert rating to percentage
                bar.style.setProperty('--progress', progress);

                // Set numeric rating display
                const ratingValue = bar.querySelector('.circular-progress-value');
                ratingValue.textContent = rating.toFixed(1);
            });
        });

/*
document.body.onclick = function() {
  if(!document.fullscreenElement){ 
  document.body.webkitRequestFullScreen(); }
  }
  */


   
      const splash = document.querySelector(".splash");

document.addEventListener("DOMContentLoaded" , (e)=>{
    setTimeout(()=>{
        splash.classList.add("display-none");
} , 8000);
});

