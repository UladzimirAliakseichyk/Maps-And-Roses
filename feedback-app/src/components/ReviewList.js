import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles.css';

function renderRatingStars(rating) {
  const stars = "⭐".repeat(rating);
  return stars;
}

function App() {
  const [reviews, setReviews] = useState([]);
  const [groupedReviews, setGroupedReviews] = useState({});
  const [selectedShop, setSelectedShop] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8000/api/feedback/')
      .then(response => {
        setReviews(response.data);
        const grouped = {};
        response.data.forEach(review => {
          if (grouped[review.shop]) {
            grouped[review.shop].push(review);
          } else {
            grouped[review.shop] = [review];
          }
        });
        setGroupedReviews(grouped);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  const toggleShopReviews = (shop) => {
    setSelectedShop(shop === selectedShop ? '' : shop);
  };

  const filteredReviews = selectedShop ? groupedReviews[selectedShop] : reviews;
  const reversedReviews = [...filteredReviews].reverse();

  return (
    <div className='revs-container'>
      <div>
        <div className="button-group">
          {Object.keys(groupedReviews).map(shop => (
            <button
              key={shop}
              className={`shop-button big-btn ${selectedShop === shop ? 'selected' : ''}`}
              onClick={() => toggleShopReviews(shop)}
            >
              {shop}
            </button>
          ))}
        </div>
      </div>
      <ul>
        {reversedReviews.length === 0 ? (
          <p>Пока нет ни одного отзыва. Вы можете добавить первый отзыв</p>
        ) : (
          reversedReviews.map((review) => (
            <div className='all-reviews-container' key={review.id}>
              <div className="review-container">
                <span className="user-name">{review.user}</span>
                <span className="rating">{renderRatingStars(review.rating)}</span>
                <span className="review-text">{review.review}</span>
                <span className="date">{review.date_time}</span>
              </div>
            </div>
          ))
        )}
      </ul>
    </div>
  );
}

export default App;
