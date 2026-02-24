# Arbuzova Beauty — SEO Site Structure

Nail salon, Komendantsky pr. 53к1, Primorsky district, SPb. No home visits.

## Key Files
- `query_classifier.py` — all filter/strip/hub/competitor lists + functions
- `site_architecture.txt` — current hub pages with all query assignments
- `filtered_queries.txt` — excluded queries
- `close-proximity.md` — nearby streets/JK list
- `2. deep_parse_results.xlsx` — keywords + volumes + commercialization
- `3. serp_results.xlsx` — SERP top-10
- `domain_classification.py`, `calculate_commercialization.py`, `audit_domains.py`

## Methodology
- Commercialization >= 0.35 = commercial. Hub+spoke: strip geo/transactional modifiers, 1-word=main page, 2-word=hub, 3+=long-tail→parent hub.
- Nearby geo (strip, keep): Комендантский, Пионерская, Старая Деревня, Приморский, Шуваловский, Сизова, Авиаконструкторов, Парашютная, Плесецкая, Ильюшина, ЖК Новоорловский/Шуваловский/Чистое небо, Юнтолово.
- Distant geo (filter): Звёздная, Парнас, Лесная, Приморская metro, all other SPb districts/metros, non-SPb cities.
- SERP-validated merges: медицинский+лечебный, обрезной→классический, порошковый+пудровый+дип, амбре=омбре, педикюр→main page.
- 4hands = competitor (not "4 руки" service). "без наращивания" = main page (not наращивание hub).
- укрепление ногтей = informational (filtered). коррекция отросшего = informational (filtered).
- отзыв/прайс/абонемент = content signals (strip, cluster to parent page). рейтинг = filter.
- сколько стоит/где = commercial transactional (keep, strip to parent hub).

## 28 Service Hubs (see site_architecture.txt for full query lists)
Main page, Мужской, Японский, Медицинский, Пилочный, Без покрытия, В 4 руки, Детский, Аппаратный, Втирка, Комбинированный, Классический, Пудровый, Гигиенический, Наращивание, С покрытием (+лаком), Европейский, Креативный, Акции/скидки, Снятие, Френч, Омбре, Немецкий (LCN), Спа, Корейский, Экспресс, Luxio, Пленочный, С дизайном.

## Status
- Hub identification + main page cleanup: DONE
- Next: review 3+ word queries for missing hubs, define competitor comparison pages.
