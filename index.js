const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3001;

const redis = require('redis');
const redisClient = redis.createClient({
    url: process.env.REDIS_URL || 'redis://localhost:6379'
});
redisClient.on('error', (err) => console.log('Redis Client Error', err));
redisClient.connect();


app.use(cors());
app.use(express.json());

// In-memory data store
let items = [
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' },
    { id: 3, name: 'Item 3' }
];

// Helper to simulate slow database query (1 second delay)
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// GET all items (simulated slow endpoint)
app.get('/api/items', async (req, res) => {
    try {
        const cachedItems = await redisClient.get('items');
        if (cachedItems) {
            return res.json(JSON.parse(cachedItems));
        }
        // Simulate database latency
        await delay(1000); 
        await redisClient.set('items', JSON.stringify(items), { EX: 60 });
        res.json(items);
    } catch (err) {
        console.error("Redis error, falling back to DB", err);
        await delay(1000);
        res.json(items);
    }
});

// GET single item
app.get('/api/items/:id', async (req, res) => {
    await delay(200); // Shorter delay for single item
    const item = items.find(i => i.id === parseInt(req.params.id));
    if (!item) return res.status(404).send('Item not found');
    res.json(item);
});

// POST new item
app.post('/api/items', (req, res) => {
    const newItem = {
        id: items.length + 1,
        name: req.body.name || `New Item ${items.length + 1}`
    };
    items.push(newItem);
    res.status(201).json(newItem);
});

// PUT update item
app.put('/api/items/:id', (req, res) => {
    const item = items.find(i => i.id === parseInt(req.params.id));
    if (!item) return res.status(404).send('Item not found');
    
    item.name = req.body.name;
    res.json(item);
});

// DELETE item
app.delete('/api/items/:id', (req, res) => {
    items = items.filter(i => i.id !== parseInt(req.params.id));
    res.status(204).send();
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
