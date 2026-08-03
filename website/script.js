(function(){
  var canvas = document.getElementById('spine');
  var ctx = canvas.getContext('2d');
  var dpr = Math.min(window.devicePixelRatio || 1, 2);

  function brassColor(){
    var el = document.documentElement;
    var dark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    var attr = el.getAttribute('data-theme');
    if (attr === 'dark') dark = true;
    if (attr === 'light') dark = false;
    return dark ? '199,154,63' : '166,121,31';
  }

  function resize(){
    var h = document.documentElement.scrollHeight;
    canvas.width = 2 * dpr;
    canvas.height = h * dpr;
    canvas.style.height = h + 'px';
    draw();
  }

  function draw(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    var color = brassColor();
    ctx.strokeStyle = 'rgba(' + color + ',0.28)';
    ctx.lineWidth = 1 * dpr;
    ctx.beginPath();
    ctx.moveTo(1 * dpr, 0);
    ctx.lineTo(1 * dpr, canvas.height);
    ctx.stroke();

    var spacing = 96 * dpr;
    var tickLen = 6 * dpr;
    ctx.strokeStyle = 'rgba(' + color + ',0.55)';
    for (var y = 0; y < canvas.height; y += spacing){
      ctx.beginPath();
      ctx.moveTo(1 * dpr - tickLen, y);
      ctx.lineTo(1 * dpr + tickLen, y);
      ctx.stroke();
    }
  }

  window.addEventListener('resize', resize);
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', draw);
  var mo = new MutationObserver(draw);
  mo.observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });

  resize();
  window.addEventListener('load', resize);
})();
