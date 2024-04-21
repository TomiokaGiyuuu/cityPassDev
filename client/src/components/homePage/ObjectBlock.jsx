import React from 'react';
import styles from '../../styles/home.module.css'

const Message = ({name, description, imageUrl, isLast=false}) => {
    return (
        <div className={styles.objectWrapper}>
            <div className={styles.object}>
                <img src={imageUrl} alt={''} className={styles.objectImg}/>
                <div className={styles.objectName}>
                    {name}
                </div>
            </div>
            {isLast ?
                <>
                    <div style={{fontWeight: 'bold', fontSize: '36px', marginLeft: '35px'}}>
                        |
                    </div>
                    <div style={{fontWeight: 'bold', fontSize: '16px'}}>Вы прибыли</div>
                </>
                :
                <div style={{fontWeight: 'bold', fontSize: '36px', marginLeft: '35px'}}>
                    |
                </div>
            }
        </div>
    );
};

export default Message;