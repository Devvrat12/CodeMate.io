chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === "EXTRACT_CODE") {
    try {
      // 📌 Extract title from LeetCode
      const title = Array.from(document.querySelectorAll('a[href^="/problems/"]'))
        .find(a => /^\d+\.\s+/.test(a.innerText))
        ?.innerText.replace(/^\d+\.\s+/, '') || "Untitled Problem";

      // 📌 Extract description
      const descriptionElement = document.querySelector('[data-track-load="description_content"]');
      const description = descriptionElement?.innerText || "Description not found.";

      // 📌 Extract code from Monaco editor
      const codeLines = Array.from(document.querySelectorAll('.view-line')).map(line => line.innerText);
      const code = codeLines.join('\n');

      // 📌 Detect selected language (fallback to Python)
      const languageDropdown = document.querySelector('.text-text-primary');
      const language = languageDropdown?.innerText.trim() || "Python";

      // ✅ Send all data back to popup
      sendResponse({ title, description, code, language });
    } catch (error) {
      console.error("❌ Extraction error:", error);
      sendResponse({ error: "Could not extract data from page." });
    }
  }

  return true; // Required for async sendResponse
});
