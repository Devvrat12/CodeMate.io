document.getElementById("analyze-btn").addEventListener("click", () => {
  // Get active tab
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.tabs.sendMessage(
      tabs[0].id,
      { type: "EXTRACT_CODE" },
      (response) => {
        // Handle failure
        if (!response || response.error) {
          document.getElementById("response").innerText = "❌ Error: Could not extract data from page.";
          return;
        }

        // Collect values
        const action = document.getElementById("action").value;
        const requestBody = {
          problem_title: response.title,
          description: response.description,
          user_code: response.code,
          language: response.language,
          action: action
        };

        // Update UI
        document.getElementById("problem-title").innerText = response.title;
        document.getElementById("response").innerText = "⏳ Loading...";

        // Send to backend
        fetch("http://127.0.0.1:8000/analyze", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(requestBody)
        })
          .then((res) => res.json())
          .then((data) => {
            document.getElementById("response").innerText = data.response || "✅ Done!";
          })
          .catch((err) => {
            document.getElementById("response").innerText = "❌ Error: " + err.message;
          });
      }
    );
  });
});
