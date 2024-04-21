import React from 'react';
import styles from '../../styles/home.module.css'

const Faq = ({value}) => {
    return (
        <div className={styles.faqBlock}>
            {value}
        </div>
    );
};

export default Faq;