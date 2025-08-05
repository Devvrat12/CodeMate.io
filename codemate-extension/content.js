chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === "EXTRACT_CODE") {
    let title = document.querySelector("h1")?.innerText || "Untitled Problem";
    let code = "";

    // Try LeetCode editor
    let leetEditor = document.querySelector('.view-lines');
    if (leetEditor) {
      code = leetEditor.innerText;
    }

    // Add support for GFG, Codeforces etc. similarly if needed

    sendResponse({ title, code });
  }
});
