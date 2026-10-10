const chatForm = document.getElementById('chat-form');
const chatMessages = document.getElementById('chat-messages');
chatForm.addEventListener('submit', async event => {
  event.preventDefault(); const input = document.getElementById('chat-question'); const question = input.value.trim(); if (!question) return;
  const userMessage = document.createElement('div'); userMessage.className = 'chat-msg user'; userMessage.textContent = question; chatMessages.append(userMessage); input.value = '';
  const pending = document.createElement('div'); pending.className = 'chat-msg'; pending.textContent = 'Thinking…'; chatMessages.append(pending); document.getElementById('chat-error').textContent = '';
  try {
    const result = await api('/ai/ask', { method: 'POST', body: JSON.stringify({ question }) });
    pending.textContent = result.answer;
    if (result.sources?.length) { const source = document.createElement('small'); source.textContent = `Sources: ${result.sources.map(item => item.source).join(', ')}`; pending.append(document.createElement('br'), source); }
  } catch (error) { pending.remove(); document.getElementById('chat-error').textContent = `${error.message}. Start the backend to use the assistant.`; }
});
