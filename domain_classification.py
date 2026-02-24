"""
Domain/URL classification rules for SERP commercialization analysis.

Categories:
  - commercial:    service providers (salons, salon aggregators, booking)
  - ecommerce:     product stores (cosmetics, beauty supplies)
  - informational: blogs, magazines, social media, encyclopedias, image search
  - unknown:       not yet classified
"""

# ── Commercial: service providers & salon aggregators ───────────────────────
COMMERCIAL_DOMAINS = {
    # Salon aggregators / directories
    "2gis.ru",
    "zoon.ru",
    "profi.ru",
    "uslugi.yandex.ru",
    "www.avito.ru",
    "m.avito.ru",
    "youla.ru",
    "www.yell.ru",
    "spb.napopravku.ru",
    "napopravku.ru",
    "prodoctorov.ru",
    "spb.youdo.com",
    "barb.pro",

    # Salon aggregators (regional)
    "spb.krasotaimedicina.ru",
    "krasotaimedicina.ru",
    "www.krasotaimedicina.ru",

    # Salon booking platforms / aggregators
    "dikidi.net",
    "dikidi.ru",
    "beauty.dikidi.ru",
    # www.yclients.com — classified via URL patterns (journal=info, nail-salon/master=commercial)
    "widget.sonline.su",

    # Deals / coupons for services
    "speterburg.biglion.ru",
    "spb.boombate.com",

    # Known salon websites
    "kistochki.ru",
    "pilkinail.ru",
    "4hands.ru",
    "4hands-lp.ru",
    "myzefirka.ru",
    "www.kleos.ru",
    "ras4eshi.ru",
    "sierra-nails.ru",
    "liksnail.ru",
    "nogtinogti.ru",
    "gurumanicura.ru",
    "amalfibeauty.ru",
    "llmanikur.ru",
    "karamel-nail.ru",
    "magnetic-salon.ru",
    "podolog78.ru",
    "nailclinic.ru",
    "rocco-barocco.ru",
    "gastronombeauty.ru",
    "salon-leona.ru",
    "ponynail.ru",
    "polubvipiter.ru",
    "polubvi.su",
    "beauty-set.ru",
    "www.cosmetologylife.ru",
    "maleynail.ru",
    "jbextension.ru",
    "citynails.studio",
    "olacenters.com",
    "max4u.ru",
    "eleven-nail.ru",
    "self-spb.ru",
    "viela-manikyur.ru",
    "veran-lash.ru",
    "artistrynail.ru",
    "superart.spb.ru",
    # madnails.ru — training courses, moved to informational
    "beautytoday.spb.ru",
    "isterika.me",
    "www.drugoymoneycure.ru",
    "hochu.me",
    "matreshkastudio.ru",
    "salonmatreshka.ru",
    "tsvet-nails.ru",
    "greenpark-spb.ru",
    "klukva-nails.ru",
    "salonmanit.ru",
    "posh-nails.ru",
    "houseofnails.ru",
    "kbeauty-studio.ru",
    # salon312.ru — moved to ecommerce (online store)
    "idol-cut.ru",
    "sk-12m.ru",
    "mylagom.ru",
    "driadaspb.ru",
    "tsarapki.ru",
    "toffynails.ru",
    "zakanail.ru",
    "mecca.ru",
    "sodanails.ru",
    "supernailspb.ru",
    "aurora-nails.ru",
    "lak-nozhnici.ru",
    "p-n.spb.ru",
    "nailtitu.ru",
    "rednails-studio.ru",
    "mywonderlook.ru",
    "mylak.ru",
    "lakcherie.ru",
    "lseven.ru",
    "setmanicure.ru",
    "www.apple-nail.ru",
    # katmarket.ru — moved to ecommerce (product store)
    "pinklemon.ru",
    "lacoco.online",
    "nikor-salon.ru",
    "junglemanicure.ru",
    "mancaveclub.ru",
    "volkovabeauty.com",
    "saharvosk.ru",
    "www.sskluxury.ru",
    "www.spnail.ru",
    "cj-co.ru",
    "check-in-beauty.ru",
    "vpechatleniya.ru",
    "flamynails.ru",
    "spb.grushka.space",
    "www.formanails.ru",
    "lime-krasota.ru",
    "salonorhideya.ru",
    "fornailsstudio.ru",
    "www.orhida.ru",
    "www.orhida.com",
    "podohomespb.ru",
    # beauty-business72.ru — moved to ecommerce (product store)
    "lcnprof.ru",
    "prostonail.com",

    # Medical clinics with manicure/podiatry services
    "www.smclinic.ru",
    "podologiya.clinic",
    "podolog112.ru",

    # Additional salons
    "tochkafamily.ru",
    "terstyle.ru",
    "xn--90a1af.xn--80aaa6bkfrbe5b.xn--p1ai",  # спа маникюр salon (punycode)

    # ── Audit batch: salons & studios ──
    "www.masters-app.ru",
    "maysalon.ru",
    "nailstogo.ru",
    "www.malinina-studio.ru",
    "tokueva.ru",
    "youdo.com",
    "palchiki.com",
    "ll-moskovskiy.ru",
    "manicureexpress.ru",
    "rarobeauty.ru",
    "marianna-aleksandrova.ru",
    "misslisse.ru",
    "serebro-nail-studio.ru",
    "miapol.ru",
    "salonkl.ru",
    "www.blessmynails.ru",
    "only-nails.pro",
    "magicroom-nm.ru",
    "topnails.studio",
    "nailmaker.bar",
    "www.emimanicure.ru",
    "kogti.studio",
    "xnails.pro",
    "hardys.one",
    "manikur-spb.ru",
    "beauty-spot.ru",
    "studiokl-spb.ru",
    "zer.ru",
    "handy.moscow",
    "base-nail.ru",
    "dj-beauty.ru",
    "saintpierre.beauty",
    "www.1nailstudio.ru",
    "studio.beauty.nails.tilda.ws",
    "www.nikolinazabota.ru",
    "martnails.ru",
    "nailburo.ru",
    "candylovely.ru",
    "mirt.me",
    "esthetic-spb.ru",
    "fornail.ru",
    "modmesto.ru",
    "www.socium-sokol.ru",
    "apelsinsalon.ru",
    "manikur-spb.ru",

    # Audit batch: booking platforms & aggregators
    "dikidi.app",
    "beauty.dikidi.net",
    "www.fresha.com",
    "krace.ru",
    "landing.mastersapp.ru",
    "likengo.ru",
    "piter.now",
    "www.frendi.ru",
    "sankt-peterburg.spravochnikov.ru",

    # Audit batch: salons abroad
    "persona-dubai.com",
    "sugar-saloon.com",
    "sugar-istanbul.com",
    "persona-antalya.com",
    "nailsunny.ae",

    # Audit batch: salons in malls
    "europe-tc.ru",
    "trk-gulliver.ru",

    # Audit batch: medical manicure/podiatry clinics
    "id-clinic.ru",
    "mc21.ru",
    "doct.ru",
    "e-rusina.ru",
    "podologchel.ru",
    "podoprof.ru",
    "nails-up.ru",
    "www.onclinic.ru",
    "spb.service-centers.ru",
}

# yandex.ru/maps is commercial, but yandex.ru/images is informational
COMMERCIAL_URL_PATTERNS = [
    "yandex.ru/maps",
    "yclients.com/nail-salon",
    "yclients.com/master",
]

# Domain suffixes that indicate commercial (salon landing pages on platforms)
COMMERCIAL_DOMAIN_SUFFIXES = [
    ".clients.site",      # dikidi/yclients landing pages
    ".orgs.biz",          # business landing pages
    ".gorod812salon.ru",  # gorod812 salon network
    ".sodanails.ru",      # soda nails network
]

# ── E-commerce: product stores (NOT counted as commercial) ──────────────────
ECOMMERCE_DOMAINS = {
    # Major marketplaces
    "www.ozon.ru",
    "www.wildberries.ru",
    "market.yandex.ru",
    "aliexpress.ru",
    "www.sima-land.ru",
    "www.100sp.ru",
    "www.galacentre.ru",

    # Beauty / cosmetics stores
    "goldapple.ru",
    "rivegauche.ru",
    "www.letu.ru",
    "randewoo.ru",

    # Professional nail / beauty supplies
    "imkosmetik.com",
    "krasotkapro.ru",
    "www.krasotkapro.ru",
    "www.beautyshop.ru",
    "www.beauty-shop.ru",
    "sterille-store.ru",
    "masura.ru",
    "nails-mag.ru",
    "gelopt.ru",
    "neonail.ru",
    "odiva.ru",
    "www.hameleon-market.ru",
    "nailico.ru",
    "nail-republic.shop",
    "ingardenshop.ru",
    "ecolat.shop",
    "aravia-prof.ru",
    "parisnail.ru",
    "frenchnails.ru",
    "lcnshop.ru",
    "myslitsky-nail.ru",
    "palitra24.ru",
    "nailgoods.ru",
    "kosmetika-proff.ru",
    "gurunail.ru",
    "esteticshop.ru",
    "50den.ru",
    "algebrabeauty.ru",
    "chistovie.ru",
    "kmiz-online.ru",
    "p-shine.ru",
    "matsumi.shop",
    "japanshop.spb.ru",
    "cosmonail.art",
    "smetico.ru",

    # Salon furniture / equipment
    "www.prosalon-store.ru",
    "beautyempire.shop",
    "lemurprof.ru",
    "profreshenie.net",
    "verakso.ru",

    # Jewelry / fashion
    # sunlight.net — moved to informational (all SERP pages are /wiki/ editorial articles, not product pages)
    "www.alltime.ru",
    "www.585zolotoy.ru",
    "zolotoy.ru",
    "www.lamoda.ru",

    # Other retail
    "www.eldorado.ru",
    "www.fitmost.ru",
    "dolyame.ru",

    # ── Audit batch: nail/beauty product stores ──
    "strong-korea.ru",
    "www.proficosmetics.ru",
    "emi-shop.ru",
    "www.podrygka.ru",
    "kristallnails.ru",
    "promanicur.ru",
    "www.starnail-shop.ru",
    "www.metzger.ru",
    "www.medkv.ru",
    "www.vsalon24.ru",
    "tnlpro.com",
    "strong-nails.ru",
    "nailbox.ru",
    "emi-official.ru",
    "marathon-saeyang.ru",
    "pili-shop.ru",
    "spb.nail-industry.ru",
    "proficana.ru",
    "www.planet-nails.ru",
    "www.sunuv.su",
    "topshopnails.ru",
    "spb.nail-drill.ru",
    "integral54.ru",
    "okinail.ru",
    "divua-cosmetic.ru",
    "www.rstart.ru",
    "www.artex.ltd",
    "www.kaneprofessional.com",
    "pnbshop.com",
    "beauty-prestige.ru",
    "medlovestore.ru",
    "plastek-shop.ru",
    "grattol-official.ru",
    "elize.ru",
    "www.nogtishop.ru",
    "www.mebelit-prof.ru",
    "planeta-sirius.spb.ru",
    "www.vseinstrumenti.ru",
    "cosmetic.magnit.ru",
    "donajerdona.ru",
    "www.officemag.ru",
    "rudesignshop.ru",
    "sims-market.ru",
    "dibidishop.ru",
    "globalfashion.ru",

    # Last unknowns → ecommerce
    "www.imin.ru",       # sells pedicure/manicure equipment
    "usmall.ru",         # marketplace selling gel pads
    "beauty-business72.ru",  # P.Shine product store
    "katmarket.ru",          # nail supply store
    "salon312.ru",           # online nail supply store
}

# ── Informational: blogs, magazines, social media, etc. ────────────────────
INFORMATIONAL_DOMAINS = {
    # Social media
    "ru.pinterest.com",
    "pinterest.com",
    "www.pinterest.com",
    "www.pinterest.ru",
    "vk.com",
    "vk.link",
    "ok.ru",
    "m.ok.ru",
    "t.me",
    "www.tiktok.com",
    "tiktok.com",
    "pikabu.ru",

    # Video platforms
    "www.youtube.com",
    "youtube.com",
    "rutube.ru",

    # Encyclopedias & how-to
    "ru.wikipedia.org",
    "wikipedia.org",
    "ru.wikihow.com",

    # Blog platforms & UGC
    "dzen.ru",
    "www.dzen.ru",
    "vc.ru",
    "dtf.ru",
    "tenchat.ru",

    # Q&A platforms
    "otvet.mail.ru",
    "www.bolshoyvopros.ru",

    # News & magazines
    "lenta.ru",
    "www.novochag.ru",
    "www.marieclaire.ru",
    "style.rbc.ru",
    "www.rbc.ru",
    "www.grazia.ru",
    "lady.mail.ru",
    "deti.mail.ru",
    "hi-tech.mail.ru",
    "lisa.ru",
    "www.woman.ru",
    "thegirl.ru",
    "tv-gubernia.ru",
    "www.thevoicemag.ru",
    "t-j.ru",
    "www.fontanka.ru",
    "www.gazetametro.ru",
    "life.ru",
    "www.1obl.ru",
    "www.cosmo.ru",
    "www.glamour.ru",
    "www.wonderzine.com",
    "www.kp.ru",
    "www.pravda.ru",
    "www.chita.ru",
    "aif.ru",
    "aif.by",
    "ria.ru",
    "rg.ru",
    "iz.ru",
    "ura.news",
    "altapress.ru",
    "www.mk.ru",
    "www.nn.ru",
    "klops.ru",
    "72.ru",
    "www.vesti.ru",
    "www.m24.ru",
    "www.gazeta.ru",
    "7days.ru",
    "daily.afisha.ru",
    "peopletalk.ru",
    "krsk.aif.ru",
    "eaomedia.ru",
    "www.hibiny.ru",
    "www.vokrugsveta.ru",

    # Review sites
    "irecommend.ru",
    "otzovik.com",
    "spb.flamp.ru",
    "spb.ayle.ru",
    "markakachestva.ru",

    # Fashion/culture/lifestyle magazines & blogs
    "www.thesymbol.ru",
    "theblueprint.ru",
    "www.yapokupayu.ru",
    # nails-up.ru — moved to commercial (salon pages), /blog/ handled by URL pattern as informational
    "weddywood.ru",
    "tornado-fan.ru",
    "sinail.ru",
    "www.baby.ru",
    "www.babyblog.ru",
    "burdastyle.ru",
    "makeup.ru",
    "list-kalendarya.ru",
    "media.halvacard.ru",
    "flacon-magazine.com",
    "www.boyarovweddings.ru",
    "beautyhack.ru",
    "www.beautyinsider.ru",
    "www.kleo.ru",
    "sunmag.me",
    "super.ru",
    "voyagemagazine.ru",
    "sheglowvibe.com",
    "du.moscow",
    "www.byrdie.com",
    "www.whowhatwear.com",
    "star-tex.ru",
    "umagazine.ru",
    "www.kinoafisha.info",
    "istylemag.com",
    "lifehacker.ru",
    "woman.rambler.ru",

    # Beauty/nail blogs & info portals
    # podoprof.ru — moved to commercial (medical manicure service)
    "www.anna-key.ru",
    "modnail.ru",
    "nailsworld.ru",
    "kosmetista.ru",
    "rosilak.ru",
    "opzia.ru",
    "mirkosm.ru",
    "nemirova.pro",
    "mymanikuroff.ru",
    "ash2o.ru",
    "hoods.anvikor.ru",
    "unogel.ru",
    "lovely-nails.pro",
    "plnail.ru",
    "trendory.ru",
    "sakwa.ru",
    "amarylis.ru",
    "cosmake.by",
    "1estet.com",
    "lkrasota.ru",

    # Medical / health info
    "sprosivracha.com",
    "citilab.ru",
    "apteka.ru",
    "doctu.ru",
    "medaboutme.ru",
    "enterosgel.ru",
    "suprastinex.ru",
    "euromednsk.ru",
    "www.invitro.ru",
    "probolezny.ru",
    "nadejdamed.ru",
    "www.medicina.ru",
    "zn48.ru",
    "progen.ru",
    "w-stom.ru",
    "podologe.ru",
    "www.cnmt.ru",
    "mknc.ru",
    "stolichki.ru",

    # Gov / official
    "72.rospotrebnadzor.ru",
    "71.rospotrebnadzor.ru",
    "73.rospotrebnadzor.ru",

    # Business / marketing / career
    "www.sostav.ru",
    "www.reg.ru",
    "salon1c.ru",
    "direct.yandex.ru",
    "career.hh.ru",
    "www.sravni.ru",
    "edu.sravni.ru",
    "e-kontur.ru",
    "stilito.ru",
    "burlesque-nail.ru",

    # Stock images
    "ru.freepik.com",
    "freepik.com",
    "www.shutterstock.com",
    "www.istockphoto.com",

    # Astrology / calendars
    "astrohelper.ru",
    "sakh.online",
    "skysages.com",
    "sputnik.by",
    "goroskop-365.ru",
    "silaprimet.ru",
    "art-profi.com",
    "www.r-ulybka.ru",
    "www.yuga.ru",
    "slight.by",

    # Yandex services (not maps)
    "yandex.ru",
    "tr-page.yandex.ru",
    "tel.yandex.by",
    "reviews.yandex.ru",

    # Religion
    "islam.global",
    "islam.ru",
    "umma.ru",
    "m.islam-today.ru",
    "azan.kz",

    # Entertainment
    "www.kinopoisk.ru",
    "finuslugi.ru",
    "life.akbars.ru",
    "prosto.rabota.ru",
    "subbota.tv",
    "premier.one",
    "eva.ru",

    # Real estate (for salon rental queries)
    "spb.cian.ru",
    "spacesbc.ru",

    # Education
    "www.litres.ru",
    "www.livelib.ru",
    "perspektivadpo.ru",
    "aelita-imidg.ru",
    "medprofexpert.ru",
    "medcentr-sitimed.ru",

    # Coworking / competitions
    "propodo.ru",
    "xpnailfest.ru",
    "stellarchampionships.ru",

    # Forums / gratitude
    "gratefulhearts.ru",
    "forumlands.ru",

    # Telegram search
    "tgstat.ru",
    "tlgbot.ru",
    "tgramsearch.com",

    # Misc info/blogs
    "beautybro.ru",
    "www.kommersant.ru",
    "mama.ru",
    "www.kiz.ru",
    "spid.ru",
    "xn--80ajkddjlmjcmcn7jua.xn--p1ai",    # punycode nail blog
    "xn--b1acd3aibadcc7a8h.xn--p1ai",       # punycode nail blog
    "p-shine.co.jp",
    "taplink.cc",

    # Various
    "safina.by",
    "www.nur.kz",
    "www.sb.by",
    "bpw.style",
    "apps.apple.com",
    "www.rustore.ru",
    "club.dns-shop.ru",
    "callfilter.app",
    "app.beautyagent.ru",
    "zakon.ru",
    "journal.sovcombank.ru",
    "www.airtasker.com",
    "emionline.ru",
    "www.zdrav.ru",
    "beauty-business.ru",
    "madnails.ru",
    "valera.ai",
    "dancecolor.ru",

    # ── Audit batch: informational sites ──

    # Dictionaries / linguistics / crosswords
    "sinonim.org",
    "gramota.ru",
    "frazbor.ru",
    "fonetika.su",
    "kartaslov.ru",
    "vslovarike.ru",
    "fonetic.textologia.ru",
    "multiurok.ru",
    "www.graycell.ru",
    "poncy.ru",
    "makeword.ru",
    "scanwordhelper.ru",
    "translate.academic.ru",
    "www.translate.ru",
    "context.reverso.net",
    "odnokor.ru",
    "ru.wiktionary.org",

    # Design tools / templates
    "printut.com",
    "supa.ru",
    "drawcon.ru",
    "smmplanner.com",

    # Business / career / legal / finance
    "vechkasov.ru",
    "sky.pro",
    "spb.hh.ru",
    "office.ru",
    "alfabank.ru",
    "kurs.alfabank.ru",
    "www.consultant.ru",
    "www.regberry.ru",
    "astral.ru",
    "www.vtb.ru",
    "kontur.ru",
    "its.1c.ru",
    "patent.nalog.ru",
    "okved.tochka.com",
    "konsol.pro",
    "spark.ru",
    "pravoved.ru",
    "pos-center.ru",
    "russia.gorodrabot.ru",
    "sankt-peterburg.gorodrabot.ru",
    "spb.superjob.ru",
    "promo.yookassa.ru",

    # Beauty / nail blogs & info portals (audit batch)
    "colbacolorbar.ru",
    "tochka-krasoty.com",
    "www.probeautyspace.com",
    "nailart.online",
    "lesnails.pro",
    "masterakrasoti.ru",
    "msk.liksnail.ru",
    "4uprof.ru",
    "nange.ru",
    "arenaseo.ru",
    "blog.eleven-nail.ru",
    "nzh.by",
    "eleganzavogue.com",
    "filin-school.ru",
    "skem.ru",
    "socrimea.ru",
    "unilook-collection.ru",
    "heroine.ru",
    "shtuchki.pro",
    "tersta.ru",
    "tobiash.ru",
    "clatch.app",
    "domix.pro",
    "gigi.click",
    "x-medica.ru",

    # Training schools / courses (informational)
    "ecolespb.ru",
    "advancenails.ru",
    "prestige-kurs.ru",
    "shkola-krasoti.ru",
    "kurs-spb.ru",
    "onskills.ru",
    "perfectspb.com",
    "tehstd.ru",
    "kubshm.ru",
    "ncpo.ru",
    "postupi.online",
    "stepik.org",
    "www.razvitie-manikur.ru",
    "www.asgol.pro",
    "adems.ru",
    "foxservice.moscow",
    "z-v-c.ru",
    "uc-asor.ru",
    "spb.victoryco.ru",
    "xn--80ajpfhbgomfh1b.xn--p1ai",
    "xn--l1aks.74.xn--b1aew.xn--p1ai",
    "ohnice.ru",
    "emi-courses.ru",

    # News / media (regional & general, audit batch)
    "74.ru",
    "ngs.ru",
    "sakhalinmedia.ru",
    "pg21.ru",
    "www.rostov.kp.ru",
    "ekb.plus.rbc.ru",
    "www.sobaka.ru",
    "doctorpiter.ru",
    "www.5-tv.ru",
    "www.1tv.ru",
    "www.pravilamag.ru",
    "peterburg2.ru",
    "lgz.ru",
    "www.krsk.kp.ru",
    "ircity.ru",
    "moe-online.ru",
    "newstracker.ru",
    "78.ru",
    "29.ru",
    "v1.ru",
    "moslenta.ru",
    "1yar.tv",
    "www.gorodche.ru",
    "vesti-yamal.ru",
    "finance.rambler.ru",
    "realty.rbc.ru",
    "news.rambler.ru",

    # Magazines / lifestyle (audit batch)
    "www.psychologies.ru",
    "food.ru",
    "www.parents.ru",
    "www.mentoday.ru",
    "www.wmj.ru",
    "www.elle.com",
    "www.allure.com",
    "thefair.ru",
    "femmie.ru",
    "spletnik.ru",
    "lady.pravda.ru",
    "twizz.ru",
    "www.gastronom.ru",
    "585svadba.ru",
    "www.wedding-magazine.ru",
    "porusski.me",

    # Medical / health info (audit batch)
    "megapteka.ru",
    "doctor.rambler.ru",
    "klinikabudzdorov.ru",
    "meduniver.com",
    "gemotest.ru",
    "health.mail.ru",
    "www.mediasphera.ru",
    "souz-med.ru",
    "cmo-med.ru",
    "mag.103.by",
    "oncokdc.ru",
    "viterramed.ru",
    "muzgkb.ru",
    "www.smclinic-spb.ru",
    "medlineservice.ru",
    "klinikaluch.ru",
    "hemonc.ru",
    "comfort.sovamed.ru",
    "elamed.com",
    "dgp6-omsk.ru",
    "www.niioncologii.ru",
    "spb.benevobis.su",
    "plasticacenter.ru",
    "unionclinic.ru",

    # Government / regulatory (audit batch)
    "www.garant.ru",
    "sudact.ru",
    "fbuz11.ru",
    "www.59fbuz.ru",
    "kamenskiy.gosuslugi.ru",
    "pskovkvd.gosuslugi.ru",
    "to.orb.ru",
    "bz.orb.ru",
    "spmag.ru",

    # Religion (audit batch)
    "islamdag.ru",
    "cmn.kz",
    "islam.by",
    "daura.link",
    "mom.life",
    "ummet.kz",
    "islam.uz",

    # Interior design for salons
    "dizayn-buro.ru",
    "design-in.ru",

    # Encyclopedias (audit batch)
    "en.wikipedia.org",
    "ru.ruwiki.ru",
    "www.wikihow.com",

    # Entertainment / cinema / music / humor
    "www.ivi.ru",
    "hd.kinopoisk.ru",
    "www.kino-teatr.ru",
    "www.film.ru",
    "genius.com",
    "hitmos.me",
    "my.mail.ru",
    "music.yandex.ru",
    "vkvideo.ru",
    "300.ya.ru",
    "shytok.net",
    "www.anekdot.ru",
    "citaty.info",
    "www.inpearls.ru",
    "vse-shutochki.ru",
    "anekdoty.ru",
    "www.pozdravok.com",
    "www.litprichal.ru",
    "www.pozdravik.ru",
    "stihi.ru",
    "uquiz.com",
    "trikky.ru",
    "emojiterra.com",
    "nickfinder.com",

    # Gaming (Sims mods)
    "www.playground.ru",
    "thesimsclub.net",
    "sims4pack.ru",
    "www.thesimsresource.com",
    "www.thegamer.com",
    "www.simsfinds.com",

    # Astrology / horoscopes / dream interpretation
    "www.astromeridian.ru",
    "enigma-project.ru",
    "vedmochka.net",
    "rivendel.ru",
    "my-calend.ru",
    "beautydream.ru",
    "horoscopes.rambler.ru",
    "newyear.novochag.ru",

    # AI-generated content
    "shedevrum.ai",
    "revvy.ai",

    # Marketing / salon business advice
    "girafffe.ru",
    "pro-promotion.ru",
    "martrending.ru",
    "intrigue.dating",
    "evgeniykot.ru",
    "sloganza.ru",
    "klnv.ru",
    "arnica-crm.ru",
    "xn--80aapgyievp4gwb.xn--p1ai",
    "xn--90aauzrd9dq.xn--p1ai",

    # PPT / presentations
    "ppt-online.org",

    # City guides
    "kudago.com",
    "flowwow.com",

    # Stock images (audit batch)
    "www.freepik.com",
    "www.vecteezy.com",
    "artovrag.com",

    # Real estate / business advice
    "realty.yandex.ru",

    # Image bookmarking
    "postila.ru",

    # Forums
    "forum.aromarti.ru",
    "forum.baby.ru",
    "u-mama.ru",
    "www.guitaristka.ru",

    # Misc informational (audit batch)
    "www.ardl.ru",
    "milliard.tatar",
    "www.klerk.ru",
    "www.expertcen.ru",
    "journal.citilink.ru",
    "dvesoroki.by",
    "redsale.by",
    "makeup.kz",
    "blog.olx.kz",
    "dnr.red",
    "7hands.com",
    "adme.media",
    "habr.com",
    "naked-science.ru",
    "rozetked.me",
    "burninghut.ru",
    "web.archive.org",
    "reads.alibaba.com",
    "le-kole.ru",
    "www.www.nayada-magazin.com",
    "www.nayada-magazin.com",
    "modernus.ru",
    "www.kristally-strazy.ru",
    "pro-vzglyad.ru",
    "mel.fm",
    "prostie-r.ru",
    "monplezir.shop",
    "gnk-shop.ru",
    "odezhda.guru",
    "app.emionline.ru",
    "uteka.ru",

    # Last 9 unknowns
    "yypronail.ru",                            # nail congress/event → informational
    "www.xn--80aaufgddxe3b6cd.xn--p1ai",      # equipment repair training
    "muzgkb1.ru",                              # medical article about nails
    "mst.center",                              # informational article
    "www.runsom.com",                           # nail size chart reference
    "www.livemaster.ru",                        # craft marketplace / tutorials
    "pikinail.ru",                              # blog article about sterilization
    "sunlight.net",                             # jewelry store but all SERP pages are /wiki/ editorial nail articles
}

INFORMATIONAL_URL_PATTERNS = [
    "yandex.ru/images",
    "yandex.ru/video",
    "yclients.com/journal",
    "nails-up.ru/blog",
]

# Domain suffixes that indicate informational (Pinterest country subdomains)
INFORMATIONAL_DOMAIN_SUFFIXES = [
    ".pinterest.com",
    ".pinterest.com.au",
    "rospotrebnadzor.ru",
    ".gosweb.gosuslugi.ru",
    ".trkcontinent.ru",
    ".gosuslugi.ru",
    ".rambler.ru",
    ".kp.ru",
]

# Known Yandex search result patterns (translated pages, etc.)
INFORMATIONAL_DOMAIN_PATTERNS = [
    "pinterest.",     # any pinterest subdomain
]


def classify(domain: str, url: str = "", title: str = "") -> str:
    """
    Classify a domain/URL into: commercial, ecommerce, informational, unknown.
    """
    domain = domain.lower().strip()
    url = url.lower().strip()
    title_lower = title.lower().strip()

    # Check URL patterns first (more specific than domain)
    for pattern in COMMERCIAL_URL_PATTERNS:
        if pattern in url:
            return "commercial"

    for pattern in INFORMATIONAL_URL_PATTERNS:
        if pattern in url:
            return "informational"

    # vk.com: check title for salon/studio keywords before falling through to informational
    if domain == "vk.com":
        _commercial_title_kw = (
            "студи", "салон", "мастер маникюр", "мастер педикюр",
            "ногтев", "запись на маникюр", "запись на педикюр",
        )
        for kw in _commercial_title_kw:
            if kw in title_lower:
                return "commercial"
        return "informational"

    # Check domain sets
    if domain in COMMERCIAL_DOMAINS:
        return "commercial"

    if domain in ECOMMERCE_DOMAINS:
        return "ecommerce"

    if domain in INFORMATIONAL_DOMAINS:
        return "informational"

    # Check domain suffix patterns
    for suffix in COMMERCIAL_DOMAIN_SUFFIXES:
        if domain.endswith(suffix):
            return "commercial"

    for suffix in INFORMATIONAL_DOMAIN_SUFFIXES:
        if domain.endswith(suffix):
            return "informational"

    # Pinterest country subdomains (ca.pinterest.com, de.pinterest.com, etc.)
    if "pinterest." in domain:
        return "informational"

    return "unknown"
