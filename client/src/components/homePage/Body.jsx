import React, {useState} from 'react';
import styles from '../../styles/home.module.css'
import Faq from "./Faq.jsx";
import SendIcon from '@mui/icons-material/Send';
import Message from "./Message.jsx";
import ObjectBlock from "./ObjectBlock.jsx";


const Body = () => {
    const infoData = [
        {
            value: 'Достопримечательности Астаны'
        },
        {
            value: 'Культурные заведения'
        },
        {
            value: 'Достопримечательности Астаны'
        },
        {
            value: 'Культурные заведения'
        },
    ]
    const [value, setValue] = useState('');
    const [chatData, setChatData] = useState([]);
    const [loading, setLoading] = useState(false);

    const jsonValue = {
        prompt: value
    }
    const options = {
        method: 'POST',
        body: JSON.stringify(jsonValue)
    }

    const onChange = (e) => {
        setValue(e.target.value);
    };

    const submitText = async () => {
        setChatData([...chatData, value]);
        setValue('');
        setLoading(true);
        const response = await fetch('http://127.0.0.1:8000/chatbot/chat/', options)
            .then(response => response.json())
            .catch(error => console.error(error));

        setLoading(false);
        setChatData(prevChatData => [...prevChatData, response.answer]);

        console.log(response);
    }

    return (
        <div className={styles.bodyWrapper}>
            <div className={styles.bodyHello}>
                <h1>
                    Здравствуйте!
                </h1>
                <h2>
                    Я ваш личный путеводитель <span>CITYPASS</span>
                </h2>
                <h3>
                    Чем я могу вам помочь?
                </h3>
                {
                    chatData == [] ?
                        <div className={styles.faqWrapper}>
                            {infoData.map((elem, index) => {
                                return <Faq key={index} value={elem.value}/>
                            })}
                        </div>
                        : null
                }
                <div className={styles.messageBlock}>
                    {chatData?.map((elem, index) => {
                        return <Message
                            key={index}
                            number={index}
                            text={elem}/>
                    })}
                    {loading && <Message
                            text={'Обрабатываем запрос...'}
                            number={1}
                    />
                    }
                    {/*{objects.map((elem, index) => {*/}
                    {/*    return <ObjectBlock*/}
                    {/*        key={index}*/}
                    {/*        name={elem.name}*/}
                    {/*        description={elem.description}*/}
                    {/*        imageUrl={elem.imageUrl}*/}
                    {/*        isLast={index === objects.length - 1}*/}
                    {/*    />*/}
                    {/*})}*/}
                </div>
                <div className={styles.inputWrapper}>
                    <input className={styles.mainInput}
                           value={value}
                           onChange={onChange}
                           type="text"
                           placeholder={'Введите запрос'}/>
                    <SendIcon onClick={submitText} className={styles.inputSend}/>
                </div>
            </div>
        </div>
    );
};

export default Body;