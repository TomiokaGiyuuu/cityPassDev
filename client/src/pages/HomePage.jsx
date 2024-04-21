import React, {useEffect, useState} from 'react';
import Header from "../components/homePage/Header.jsx";
import Body from "../components/homePage/Body.jsx";

const HomePage = () => {
    const [position, setPosition] = useState({ latitude: null, longitude: null });

    useEffect(() => {
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(function (position) {
                setPosition({
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                });
            });
        } else {
            console.log("Geolocation is not available in your browser.");
        }
    }, []);
    console.log(position);

    return (
        <div>
            <Header/>
            <Body/>
        </div>
    );
};

export default HomePage;