let counter = 0;

export default async function handler(request, response) {
  // Установка заголовков CORS
  response.setHeader('Access-Control-Allow-Origin', '*');
  response.setHeader('Content-Type', 'application/json');

  if (request.method === 'GET') {
    return response.status(200).json({ count: counter });
  }

  if (request.method === 'POST') {
    counter += 1;
    return response.status(200).json({ count: counter });
  }

  return response.status(405).json({ error: 'Method not allowed' });
}