document.getElementById("analyze-btn").addEventListener("click", () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(tabs[0].id, { type: "EXTRACT_CODE" }, (response) => {
      if (!response || response.error) {
        document.getElementById("response").innerText = "❌ Error: Could not extract data from page.";
        return;
      }

      const action = document.getElementById("action").value;
      const requestBody = {
        problem_title: response.title,
        user_code: response.code,
        description: response.description,  // 🔥 include the full description
        action: action
      };

      document.getElementById("problem-title").innerText = response.title;
      document.getElementById("response").innerText = "⏳ Loading...";

      fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestBody)
      })
        .then((res) => res.json())
        .then((data) => {
          document.getElementById("response").innerText = data.response;
        })
        .catch((err) => {
          document.getElementById("response").innerText = "❌ Error: " + err.message;
        });
    });
  });
});
