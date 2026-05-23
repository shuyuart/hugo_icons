---
title: "{{ replace .File.ContentBaseName "-" " " | title }}"
date: {{ .Date }}
tags: []
image: "/icons/{{ index (split .File.Dir "/") 1 }}/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk.png"
---

<!-- 簡短描述這個圖示的內容，可加 <br> 換行 -->

<div class="download-group">
  <img src="/icons/{{ index (split .File.Dir "/") 1 }}/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk32.png" alt="{{ replace .File.ContentBaseName "-" " " | title }} 像素圖示（黑框版）">
  <span class="download-label">下載黑框</span>
  <div class="download-row">
    <a href="/icons/{{ index (split .File.Dir "/") 1 }}/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk.png" download class="btn-download">16x16</a>
    <a href="/icons/{{ index (split .File.Dir "/") 1 }}/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk32.png" download class="btn-download">32x32</a>
    <a href="/icons/{{ index (split .File.Dir "/") 1 }}/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk64.png" download class="btn-download">64x64</a>
    <a href="/icons/{{ index (split .File.Dir "/") 1 }}/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_bk128.png" download class="btn-download">128x128</a>
  </div>
</div>

<br>

<div class="download-group">
  <img src="/icons/{{ index (split .File.Dir "/") 1 }}/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_cr32.png" alt="{{ replace .File.ContentBaseName "-" " " | title }} 像素圖示（無框版）">
  <span class="download-label">下載無框</span>
  <div class="download-row">
    <a href="/icons/{{ index (split .File.Dir "/") 1 }}/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_cr.png" download class="btn-download">16x16</a>
    <a href="/icons/{{ index (split .File.Dir "/") 1 }}/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_cr32.png" download class="btn-download">32x32</a>
    <a href="/icons/{{ index (split .File.Dir "/") 1 }}/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_cr64.png" download class="btn-download">64x64</a>
    <a href="/icons/{{ index (split .File.Dir "/") 1 }}/{{ .File.ContentBaseName }}/{{ .File.ContentBaseName }}16_cr128.png" download class="btn-download">128x128</a>
  </div>
</div>
