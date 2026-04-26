---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
tags: []
image: "/icons/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk.png"
---

<!-- 簡短描述這個圖示的內容，可加 <br> 換行 -->

<div class="download-group">
  <img src="/icons/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk32.png" alt="{{ .File.ContentBaseName }}16_bk">
  <span class="download-label">下載黑框</span>
  <div class="download-row">
    <a href="/icons/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk.png" download class="btn-download">16x16</a>
    <a href="/icons/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk32.png" download class="btn-download">32x32</a>
    <a href="/icons/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk64.png" download class="btn-download">64x64</a>
    <a href="/icons/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk128.png" download class="btn-download">128x128</a>


  </div>
</div>

<br>

<div class="download-group">
  <img src="/icons/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_cr32.png" alt="{{ .File.ContentBaseName }}16_cr">
  <span class="download-label">下載無框</span>
  <div class="download-row">
    <a href="/icons/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_cr.png" download class="btn-download">16x16</a>
    <a href="/icons/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_cr32.png" download class="btn-download">32x32</a>
    <a href="/icons/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_cr64.png" download class="btn-download">64x64</a>
    <a href="/icons/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_cr128.png" download class="btn-download">128x128</a>
  </div>
</div>
