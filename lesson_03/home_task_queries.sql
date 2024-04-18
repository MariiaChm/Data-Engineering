/*
 Завдання на SQL до лекції 03.
 */

/*
1.
Вивести кількість фільмів в кожній категорії.
Результат відсортувати за спаданням.
*/

select
    c.name,
    count (distinct fc.film_id)
from postgres.public.film_category fc
     join postgres.public.category c on c.category_id=fc.category_id
group by c.name
order by 2 desc;

/*
2.
Вивести 10 акторів, чиї фільми брали на прокат найбільше.
Результат відсортувати за спаданням.
*/
select
    a.first_name || ' ' || a.last_name actor,
    count (rental_id)
from rental r
    join inventory i on r.inventory_id=i.inventory_id
    join film_actor fa on fa.film_id=i.film_id
    join actor a on a.actor_id=fa.actor_id
group by a.first_name || ' ' || a.last_name
order by 2 desc
limit 10;

/*
3.
Вивести категорія фільмів, на яку було витрачено найбільше грошей
в прокаті
*/

select
    c.name,
    sum(amount)
from rental r
    join inventory i on r.inventory_id=i.inventory_id
    join film_category fc on fc.film_id=i.film_id
    join category c on c.category_id=fc.category_id
    join payment p on p.rental_id=r.rental_id
group by c.name
order by 2 desc
limit 1;

/*
4.
Вивести назви фільмів, яких не має в inventory.
Запит має бути без оператора IN
*/

select distinct
    title
from film f
    left join inventory i on f.film_id=i.film_id
where i.film_id is null;

/*
5.
Вивести топ 3 актори, які найбільше зʼявлялись в категорії фільмів “Children”.
*/
select
    a.first_name || ' ' || a.last_name actor,
    count(fa.film_id)
from actor a
    join film_actor fa on fa.actor_id=a.actor_id
    join film_category fm on fm.film_id=fa.film_id
    join category c on c.category_id = fm.category_id
where c.name='Children'
group by a.first_name || ' ' || a.last_name
order by 2 desc
limit 3;
