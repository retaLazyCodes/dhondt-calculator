import { API_URL } from './settings'

const baseUrl = `${API_URL}/elections`

const getAll = async () => {
    const response = await fetch(`${baseUrl}/?order=desc`);
    if (!response.ok) {
        throw new Error('Failed to fetch data');
    }
    return await response.json();
}

const create = async (newObject) => {
    const payload = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newObject)
    };
    const response = await fetch(baseUrl, payload);
    if (!response.ok) {
        throw new Error('Failed to create data');
    }
    return await response.json();
}

const service = {
    getAll, create
}

export default service