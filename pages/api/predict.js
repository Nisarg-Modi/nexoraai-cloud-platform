export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    // Replace this URL with your currently active Serveo tunnel URL from GKE
    const KSERVE_URL = 'https://YOUR-ACTIVE-SERVEO-URL.serveousercontent.com/v1/models/fraud-model:predict';

    const response = await fetch(KSERVE_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(req.body),
    });

    const data = await response.json();
    return res.status(200).json(data);
  } catch (error) {
    return res.status(500).json({ error: 'Failed to connect to model predictor', details: error.message });
  }
}
