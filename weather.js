function askWeather() {
    const city = document.getElementById('cityInput').value || "Jaipur";
    // Hit the backend, get the forecast!
    fetch(`/weather?city=${encodeURIComponent(city)}`)
        .then(response => response.json())
        .then(info => {
            let message;
            if (info.error) {
                message = `<span style="color:red;">Sorry, couldn't fetch data: ${info.error}</span>`;
            } else {
                message = `<div>
                    <div class="label">Place:</div> ${info.place}<br/>
                    <div class="label">Temperature:</div> ${info.temperature}&deg;C<br/>
                    <div class="label">Condition:</div> ${info.summary}<br/>
                    <div class="label">Humidity:</div> ${info.humidity}%
                </div>`;
            }
            document.getElementById('weatherBox').innerHTML = message;
        })
        .catch(err => {
            document.getElementById('weatherBox').innerHTML = "<span style='color:red;'>Oops: "+err+"</span>";
        });
};
