// reportWebVitals.js
import { getCLS, getFID, getLCP, getFCP, getTTFB } from 'web-vitals';

function sendToAnalytics({ name, delta, id }) {
  // Здесь вы можете отправлять метрики в вашу аналитику или другую систему мониторинга
  console.log(name, delta, id);
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getLCP(sendToAnalytics);
getFCP(sendToAnalytics);
getTTFB(sendToAnalytics);
