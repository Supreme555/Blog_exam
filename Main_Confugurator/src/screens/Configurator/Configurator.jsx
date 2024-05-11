import React from 'react';
import styles from './Configurator.module.css'
import styles_g from '../../components/styles/Global.module.css'
import Header from '../home/components/Header/Header'
import Footer from '../home/components/Footer/Footer'
import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom';
// import { Video_cards, Processors, Materincas} from '../../../../index';
// import { Video_cards, Processors, Materincas} from './index';
import GetObj from '../../components/ui/Api';
import { apiComp } from '../../app/index';

const Configurator = () => {
    const [Video_cards, setVideo_cards] = useState(null)
    const [Processors, setProcessors] = useState(null)
    const [Materincas, setMaterincas] = useState(null)
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        const fetchData = async () => {
            try {
                await GetObj().then((comp) => {
                    setVideo_cards((apiComp(comp).payload.comp[0]))
                    setProcessors((apiComp(comp).payload.comp[1]))
                    setMaterincas((apiComp(comp).payload.comp[2]))
                })
                setLoading(false);
            } catch (error) {
                console.error('Ошибка при получении данных:', error);
                setLoading(true);
            }
        };

        fetchData();
    }, []);
    const navigate = useNavigate();
    let arr = []
    const [data, setData] = useState(arr)
    const [price, setPrice] = useState(0)
    const addComp = (newObj) => {
        setData(prevArray => [...prevArray, newObj]);
    }
    useEffect(() => {
        const newPrices = data.map(item => item.Price);
        const total = newPrices.reduce((accumulator, currentValue) => {
            return accumulator + currentValue;
        }, 0);
        setPrice(total)
    }, [data]);
    const handleKorz = () => {
        const myObject = data;
        navigate('/Cart/', { state: { myObject, price } });
    };
    const handleClear = () => {
        setData(arr)
        setPrice(0)
    }
    return (
        <div>
            <Header />
            <main className={`${styles_g.container} p-6 rounded-xl shadow-xl`}>
                <div className={`${styles.about}`}>
                    <div className={`${styles.abouttext}`}>
                        <div className={`${styles.main} `}>
                            <span className='text-2xl font-bold mb-2'>Конфигуратор системного блока онлайн</span>
                            <div className='mt-10 flex flex-row justify-between'>
                                <div className=''>
                                    <h1 className='text-2xl flex flex-row items-center'>
                                        Выберите видеокарту
                                    </h1>
                                    {/* {VideoItems} */}
                                    {
                                        loading ? (
                                            <p>Loading...</p>
                                        )
                                            : (Video_cards.map((Video_card) =>
                                                <li key={Video_card.id} className='p-4 flex flex-row space-x-12 w-11/12 mt-8 rounded-xl border-2 border-zinc-300 shadow-lg'>
                                                    <img src={Video_card.Img_url} className=' w-64 ' />
                                                    <div className=''>
                                                        <h1 className='text-2xl'>Название {Video_card.Name}</h1>
                                                        <p className='text-xl'>Обьем видео памяти: <span className='font-bold'>{Video_card.Video_memory_capacity}</span></p>
                                                        <p className='text-xl'>Цена: <span className='font-bold'>{Video_card.Price}</span></p>
                                                    </div>
                                                    <button className='transition ease-in border-2 h-1/5 text-lg p-2 rounded-2xl hover:bg-gray-200' onClick={() => addComp(Video_card)}>Добавить</button>
                                                </li>
                                            )
                                            )
                                    }
                                    <h1 className='text-2xl mt-10 flex flex-row items-center'>Выберите процессор</h1>
                                    {
                                        loading ? (
                                            <p>Loading...</p>
                                        )
                                            : (Processors.map((Processor) =>
                                                <li key={Processor.id} className='p-4 flex flex-row space-x-12 mt-8 w-11/12 rounded-xl border-2 border-zinc-300 shadow-lg'>
                                                    <img src={Processor.Img_url} className=' w-32' />
                                                    <div className='w-full'>
                                                        <h1 className='text-2xl'>Название {Processor.Name}</h1>
                                                        <p className='text-xl'>Обьем видео памяти: <span className='font-bold'>{Processor.Number_of_threads}</span></p>
                                                        <p className='text-xl'>TDP: <span className='font-bold'>{Processor.TDP}</span></p>
                                                        <p className='text-xl'>Тактовая частота: <span className='font-bold'>{Processor.Clock_frequency}</span></p>
                                                        <p className='text-xl'>Цена: <span className='font-bold'>{Processor.Price}</span></p>
                                                    </div>
                                                    <button className='border-2 mt-20 text-lg p-2 rounded-2xl hover:bg-gray-200' onClick={() => addComp(Processor)} >Добавить</button>
                                                </li>
                                            )
                                            )
                                    }
                                    <h1 className='text-2xl mt-10 flex flex-row items-center'>Выберите Материнскую плату</h1>
                                    {
                                        loading ? (
                                            <p>Loading...</p>
                                        ) : Materincas.map((Materinca) =>
                                            <li key={Materinca.id} className='p-4 flex flex-row space-x-12 mt-8 w-11/12 rounded-xl border-2 border-zinc-300 shadow-lg'>
                                                <img src={Materinca.Img_url} className='w-1/5' />
                                                <div className=''>
                                                    <h1 className='text-2xl'>Название {Materinca.Name}</h1>
                                                    <p className='text-xl'>Обьем видео памяти: <span className='font-bold'>{Materinca.Number_of_threads}</span></p>
                                                    <p className='text-xl'>Socket: <span className='font-bold'>{Materinca.Socket}</span></p>
                                                    <p className='text-xl'>Цена: <span className='font-bold'>{Materinca.Price}</span></p>
                                                </div>
                                                <button className='border-2 mt-20 text-lg p-2 rounded-2xl hover:bg-gray-200' onClick={() => addComp(Materinca)} >Добавить</button>
                                            </li>
                                        )
                                    }
                                </div>
                                <div className={`p-2 bg-gray-200 ${styles.config_manager} rounded-xl`}>
                                    <div className={styles.config_manager_in}>
                                        <h1 className='text-2xl flex flex-row items-center mb-2'>
                                            Стоимость ПК
                                        </h1>
                                        <span className='flex justify-between'>
                                            <h1 className='text-2xl flex flex-row items-center'>
                                                Итого:
                                            </h1>
                                            <h1 className='text-2xl flex flex-row items-center'>
                                                {price} ₸
                                            </h1>
                                        </span>
                                        <span className={styles.btns}>
                                            <button className={`${styles.btn} ${styles.btn_1}`} onClick={() => { handleKorz() }}>Собрать</button>
                                            <button className={`${styles.btn} ${styles.btn_2}`} onClick={() => { handleClear() }}>Очистить</button>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default Configurator;
