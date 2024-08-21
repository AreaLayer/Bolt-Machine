const apiUrl = "https://api.amboss.space/graphql";
const query = `
{
  getNode(pub_key: "your_node_pub_key") {
    alias
    capacity
    channels
  }
}`;

async function fetchNodeData() {
    const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_AMBOSS_API_TOKEN"
        },
        body: JSON.stringify({ query })
    });

    const result = await response.json();
    pushDataToPython(result.data);
}

async function pushDataToPython(data) {
    const response = await fetch('http://localhost:5000/push_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    console.log('Processed Data:', result.processed_data);
}

fetchNodeData();

