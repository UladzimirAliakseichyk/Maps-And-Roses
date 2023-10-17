import React from 'react';
import './styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Logo from './logo.svg';
import { Link } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import './styles.css';



function Header() {
  const location = useLocation();
  const navigate = useNavigate();
  const navigateToHomePage = () => {
    navigate('/'); // Перенаправляем на главную страницу
  };
  // Проверка текущего маршрута
const isLeaveReviewPage = location.pathname === '/new-review';

  return (
    <div className='header'>
        <button className='main-header-btn' onClick={navigateToHomePage}>
        <img className='logo-img' src={Logo} alt='logo' />
        <b>Maps</b> and roses</button>
        {/* Проверка текущего маршрута и скрытие кнопки при необходимости */}
        {!isLeaveReviewPage && <Link className='new-rev-btn' to="/new-review">Оставить отзыв</Link>}
      </div>
   
  );
}

export default Header;
