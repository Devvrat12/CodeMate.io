chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === "EXTRACT_CODE") {
    try {
      // Extract title
      const title = Array.from(document.querySelectorAll('a[href^="/problems/"]'))
        .find(a => a.innerText?.match(/^\d+\.\s+/))
        ?.innerText?.replace(/^\d+\.\s+/, '') || "Untitled Problem";

      // Extract full description
      const descriptionElement = document.querySelector('[data-track-load="description_content"]');
      const description = descriptionElement ? descriptionElement.innerText : "Description not found.";

      // Extract code lines from visible Monaco editor
      let codeLines = Array.from(document.querySelectorAll('.view-line')).map(line => line.innerText);
      let code = codeLines.join('\n');

      sendResponse({ title, description, code });
    } catch (err) {
      sendResponse({ error: "Could not extract data from page." });
    }
  }
  return true; // Required for async sendResponse
});
