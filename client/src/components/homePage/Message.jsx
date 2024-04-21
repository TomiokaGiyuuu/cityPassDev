import React from 'react';
import styles from '../../styles/home.module.css'
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import SmartToyIcon from '@mui/icons-material/SmartToy';

const Message = ({text, number}) => {
    return (
        <div className={styles.message}>
            {number % 2 == 0 ? <AccountCircleIcon/> : <SmartToyIcon/>}
            <div>
                {text}
            </div>
        </div>
    );
};

export default Message;