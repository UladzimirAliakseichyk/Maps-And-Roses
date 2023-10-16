import React, { useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.css';

function ReviewForm({ onReviewSubmitted }) {
  const [formData, setFormData] = useState({
    user: '',
    review: '',
    shop: '',
    rating: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleRatingClick = (rating) => {
    if (formData.rating === rating) {
      // Если уже выбрана текущая оценка, снимаем выделение
      setFormData({ ...formData, rating: '' });
    } else {
      // В противном случае, устанавливаем новую оценку
      setFormData({ ...formData, rating });
    }
  };

  const handleShopClick = (shop) => {
    if (formData.shop === shop) {
      // Если уже выбран магазин, снимаем выделение
      setFormData({ ...formData, shop: '' });
    } else {
      // В противном случае, устанавливаем новый магазин
      setFormData({ ...formData, shop });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Отправка данных на сервер (вашему API)
    axios.post('http://localhost:8000/api/feedback/', formData)
      .then((response) => {
        // Обработка успешной отправки, например, сброс формы
        setFormData({
          user: '',
          review: '',
          shop: '',
          rating: '',
        });

        onReviewSubmitted();
      })
      .catch((error) => {
        console.error('Ошибка при отправке отзыва', error);
      });
  };

  return (
    <div className="review-form">
      <h2>Оставьте свой отзыв</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <input className='name-style'
            placeholder="Имя"
            type="text"
            name="user"
            value={formData.user}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <div>
            {[1, 2, 3, 4, 5].map((rating) => (
              <button
                key={rating}
                type="button"
                className={`rating-button sml-btn ${formData.rating === rating ? 'selected' : ''}`}
                onClick={() => handleRatingClick(rating)}
              >
                {'⭐'.repeat(rating)} 
              </button>
            ))}
          </div>
        </div>

        <div className="form-group">
          <div>
            {['Дорорс', 'Розы.бел', 'rozyminsk.by', 'daflor.by', 'Яцветы'].map((shop) => (
              <button
                key={shop}
                type="button"
                className={`sml-btn shop-button ${formData.shop === shop ? 'selected' : ''}`}
                onClick={() => handleShopClick(shop)}
              >
                {shop}
              </button>
            ))}
          </div>
        </div>

        <div className="form-group">
          <textarea
            className="review-textarea"
            placeholder="Отзыв"
            name="review"
            value={formData.review}
            onChange={handleChange}
            required
          />
        </div>

        <button className="btn-submit" type="submit">
          Отправить
        </button>
      </form>
    </div>
  );
}

export default ReviewForm;
