import React, { useState } from 'react';
import ReviewForm from './ReviewForm';
import { useNavigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.css';

function LeaveReviewPage() {
  const navigate = useNavigate();
  const [reviewSubmitted, setReviewSubmitted] = useState(false);

  const handleReviewSubmitted = () => {
    // Обработка успешной отправки формы (например, отправка на сервер)
    // После успешной отправки вызывайте setReviewSubmitted(true);

    // В данном случае просто устанавливаем, что отзыв отправлен
    setReviewSubmitted(true);
  };
  const navigateToHomePage = () => {
    navigate('/'); // Перенаправляем на главную страницу
  };

  return (
    <div className='new-rev-body'>
      {reviewSubmitted ? (
        <div className='container-succes'>
          <p>Ваш отзыв успешно добавлен!</p>
          <button className='redirect-btn' onClick={navigateToHomePage}>
            Все отзывы
          </button>
        </div>
      ) : (
        <ReviewForm onReviewSubmitted={handleReviewSubmitted} />
      )}
    </div>
  );
}

export default LeaveReviewPage;
