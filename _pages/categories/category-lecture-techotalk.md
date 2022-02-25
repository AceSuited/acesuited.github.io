---
title: "우아한 테코톡"
layout: archive
permalink: categories/techotalk
author_profile: true
sidebar_main: true
---



유튜브 `우아한Tech` 채널의 __[10분 테코톡]__ 시리즈를 듣고 정리하기

{% assign posts = site.categories.techotalk %}

{% for post in posts %} {% include archive-single-custom.html type=page.entries_layout %} {% endfor %}

