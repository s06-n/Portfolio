import { useState } from 'react';
import './App.css';

function App() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [isLoggedin, setIsLoggedin] = useState(false);
    const [showUnsuccessful, setShowUnsuccessful] = useState(false);

    // Correct login details
    const predefinedUserData = {
        validUsername: 'user',
        validPassword: 'password',
    };

    const login = () => {

        // Compares input data with set user data
        if (
            username === predefinedUserData.validUsername &&
            password === predefinedUserData.validPassword
        ) {
            setIsLoggedin(true);
        } else {
            setShowUnsuccessful(true);
        }
    };

    const logout = () => {
        setIsLoggedin(false);
        setShowUnsuccessful(false);
    };

    return (
        <>
            <div className="container">
                
                {!isLoggedin && !showUnsuccessful ? (
                    <>
                    <h1 className="font">Login</h1>
                        <form action="">
                        <label className="font">Username:</label>
                            <input
                                type="text"
                                onChange={(e) => setUsername(e.target.value)}
                                value={username}
                                placeholder="Username"
                                className="font"
                            />
                            <label className="font">Password:</label>
                            <input
                                type="password"
                                onChange={(e) => setPassword(e.target.value)}
                                value={password}
                                placeholder="Password"
                                className="font"
                            />
                            <button className="font" type="submit" onClick={login}>
                                submit
                            </button>
                        </form>
                    </>
                ) : isLoggedin ? (
                    <>
                        <h1 className="font">Welcome you have successfully logged in</h1>
                        <h2 className="font">Click here to log out</h2>
                        <button className="font" onClickCapture={logout}>Logout user</button>
                    </>
                ) : (
                    <>
                        <h1 className="font">Login unsuccessful, please try again</h1>
                        <h2 className="font">Click here to go back to the login page</h2>
                        <button className="font" onClick={() => setShowUnsuccessful(false)}>Return to Login</button>
                    </>
                )}
            </div>
        </>
    );
}

export default App;