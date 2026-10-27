window.addEventListener("load", () => {

  let isDragging = false;
  let startX = 0;
  let startY = 0;

  document.addEventListener("wheel", function (e) {

    // Only act inside fullscreen container
    const container = e.target.closest(".mermaid-container-fullscreen");
    if (!container) return;

    const svg = container.querySelector("svg");
    if (!svg) return;

    e.preventDefault();

    let scale = svg.__scale || 1;
    let offsetX = svg.__offsetX || 0;
    let offsetY = svg.__offsetY || 0;

    const factor = 1.1;

    // Get mouse position relative to container
    const rect = container.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    // Convert mouse position to SVG coordinates
    const svgX = (mouseX - offsetX) / scale;
    const svgY = (mouseY - offsetY) / scale;

    // Apply zoom
    scale *= e.deltaY < 0 ? factor : 1 / factor;
    scale = Math.max(0.3, Math.min(5, scale));

    // Adjust offset so zoom happens at cursor
    offsetX = mouseX - svgX * scale;
    offsetY = mouseY - svgY * scale;

    svg.__scale = scale;
    svg.__offsetX = offsetX;
    svg.__offsetY = offsetY;

    applyTransform(svg);

  }, { passive: false });


  document.addEventListener("mousedown", function (e) {

    const container = e.target.closest(".mermaid-container-fullscreen");
    if (!container || e.button !== 0) return;

    const svg = container.querySelector("svg");
    if (!svg) return;

    isDragging = true;

    startX = e.clientX;
    startY = e.clientY;

    container.style.cursor = "grabbing";
  });


  document.addEventListener("mousemove", function (e) {

    if (!isDragging) return;

    const container = document.querySelector(".mermaid-container-fullscreen");
    if (!container) return;

    const svg = container.querySelector("svg");
    if (!svg) return;

    let offsetX = svg.__offsetX || 0;
    let offsetY = svg.__offsetY || 0;

    // Move relative to mouse movement
    offsetX += (e.clientX - startX);
    offsetY += (e.clientY - startY);

    startX = e.clientX;
    startY = e.clientY;

    svg.__offsetX = offsetX;
    svg.__offsetY = offsetY;

    applyTransform(svg);
  });


  document.addEventListener("mouseup", function () {

    isDragging = false;

    const container = document.querySelector(".mermaid-container-fullscreen");
    if (container) {
      container.style.cursor = "grab";
    }
  });


  // Double click reset
  document.addEventListener("dblclick", function (e) {

    const container = e.target.closest(".mermaid-container-fullscreen");
    if (!container) return;

    const svg = container.querySelector("svg");
    if (!svg) return;

    svg.__scale = 1;
    svg.__offsetX = 0;
    svg.__offsetY = 0;

    applyTransform(svg);
  });


  function applyTransform(svg) {

    const scale = svg.__scale || 1;
    const offsetX = svg.__offsetX || 0;
    const offsetY = svg.__offsetY || 0;

    svg.style.transform =
      `translate(${offsetX}px, ${offsetY}px) scale(${scale})`;

    svg.style.transformOrigin = "0 0";
  }

});