import tkinter as tk
from tkinter import ttk
from tkinter import ttk, StringVar, PhotoImage
from tkinter import font as tkfont

# Base de conocimientos con reglas definidas
reglas = {
   'Regla 1': {
        'sintomas': 'baja critica a comentarios negativos y criticas',
        'diagnostico': 'Alta sensibilidad emocional',
        'recomendaciones': '\n1.Practiva la empatia activa: escucha acticvamente y valida sus emociones\n2.Respeta los limites personales: respeta tus necsidades de tiempo a solas y no lo tomes algo personal\n3.Fomentan ambiente de seguridad y confinza  '
    },
    'Regla 2': {
        'sintomas': 'Me frustro con facilidad ante proyectos y tareas cotidianas o demás',
        'diagnostico': 'Baja tolerancia a la frustración',
        'recomendaciones': '\n1.Estable metas realistas para tu vida\n2.Piena en si tienes alguna creencia irracional\n3.Analiza que situaciones son las que te generan mas frustaciones y ponlas en practica '
    },
    'Regla 3': {
        'sintomas': 'necesidad de comentarios positivos, halagos y redes sociales',
        'diagnostico': 'necesidad constante de validación',
        'recomendaciones': '\n1Trabaja en tu autoestima y busca actividades que disfrutes\n2.Técnicas de mindfulness\n3Entrenar algun deporte de tu preferencia',
    },
    'Regla 4': {
        'sintomas': 'no me gusta enfrentar problemas personales o otros problemas',
        'diagnostico': 'auto-censura, evasión de temas delicados',
        'recomendaciones': '\n1.Considera hablar con un profesional sobre tus emociones \n2. Toma practicas de meditación que te ayuden a autoconocerte\n3.Haz una lista donde puedas llevar el control de todas tus emociones semanales ',
    },
    'Regla 5': {
        'sintomas': 'miedo a que una foto dañe mi imagen personal',
        'diagnostico': 'Preocupación por la imagen en redes sociales',
        'recomendaciones': '\nLimita tu tiempo en redes y enfócate en lo positivo\n2. Enfoca tu tiempo libre en actividades didacticas \n3. Dedicale más tiempo a tu familia y deberes cotidianos ',
    },
    'Regla 6': {
        'sintomas': 'preocupación por cosas que no han pasado y sobrepienso lo que puede llegar a pasar',
        'diagnostico': 'sentimiento de ansiedad',
        'recomendaciones': '\nPractica técnicas de respiración y considera el ejercicio regular\n2.Realiza más ejercicio para tener un cuerpo y una mente sana\n3.Invierte tu tiempo libre en pintar, bailar, cantar, etc',
    },
    'Regla 9': {
        'sintomas': 'siento tristeza y vacío interior y desesperanza, lo que puede afectar mi estado de ánimo y cómo me siento',
        'diagnostico': 'Depresión',
        'recomendaciones': '\nBusca apoyo emocional y considera la terapia.\n2 Trata de no pasar tanto tiempo a solas\n3 Busca refugio con algun amigo o familiar'
    },
    'Regla 10': {
        'sintomas': 'siento una sensación de inseguridad e insuficiencia, y tengo dificultades para manejar situaciones estresantes',
        'diagnostico': 'Baja autoestima',
        'recomendaciones': '\nDedica tiempo a tus habilidades y establece pequeños logros.\n2Elabora una pequeña lista con actividades que puedes hacer en el día para mantenerte ocupad@\n3Leer libros de autoayuda',
    },
     'Regla 11': {
        'sintomas': 'me siento fatigado, se me acelera el corazón, y tengo la sensación de aburrimiento. me altero y me siento raro',
        'diagnostico': 'Dificultades para manejar el estrés',
        'recomendaciones': '\n1.Sal a caminar minimo 1 hora diaria y respirar aire puro\n2.Terapias o grupos de apoyos \n3.Socialización y compasión con demás personas de tu entorno',
    },
    'Regla 12': {
        'sintomas': 'no tengo un pensamiento adecuado para poner ciertas barreras a las personas',
        'diagnostico': 'Dificultades para establecer fronteras',
        'recomendaciones': '\n1.Practica tipos de afirmaciones positivas\n2. Realiza un diario personal\n3.Busca lugares donde te puedas presentar como voluntariado',
    },
    'Regla 13': {
        'sintomas': 'por cada cosa que hago o digo siento que está mal, como si realmente lo hubiera hecho mal',
        'diagnostico': 'Culpa y vergüenza',
        'recomendaciones': '\n1.Socializar más con tu entorno diario\n2. Estable en tu diario pequeñas metas\n3.Parate al frente de tu espejo y repite palabras positivas hacia tí',
    },
    'Regla 14': {
        'sintomas': 'no me siento capacitado para tomar decisiones y tengo miedo a equivocarme y a la presión de cumplir expectativas',
        'diagnostico': 'Problemas para tomar decisiones',
        'recomendaciones': '\n1.Investiga-profundiza más sobre el tema\n2. Establece criterios que puedes ayudarte a buscar una solución adecuada\n3.Empieza una pequeña rutina de Journaling '
    },
    'Regla 15': {
        'sintomas': 'me retiro de las personas porque no siento que les agrade o me preocupo por el juicio ajeno y no quiero hablar con nadie',
        'diagnostico': 'Aislamiento social',
        'recomendaciones': '\n1.Leer libros de autoayuda emocional\n2.Crea una lista de pro y contra de tu conducta\n3. Buscar ayuda profesional',
    },
    'Regla 16': {
        'sintomas': 'me guardo cada cosa que me pasa sin decir o expresar una emoción',
        'diagnostico': 'Dificultades en la regulación emocional',
        'recomendaciones': '\n1.Terapia o asesoramiento de un profesinal\n2. Practica ejercicio \n3. Realiza 1 hora de caminata al día para desestresarte'
    },
    'Regla 17': {
        'sintomas': 'tengo miedo constante a ser juzgado o a no cumplir con las normas sociales y expectativas',
        'diagnostico': 'Preocupaciones sobre la percepsión social',
        'recomendaciones': '\n1.Ir a terapias o grupos de apoyo\n2.Practica de talleres de habilidades sociales\n3. Realiza cualquier técnica de relajación',
    },
    'Regla 18': {   
        'sintomas': 'me siento muy agobiad@ por clases, familia, amigos ',
        'diagnostico': 'Estres cronico',
        'recomendaciones': '\n1.Caminar o trotar\n2. Un gran baño de hidroterapia\n3.Realizar cualquier tipo de actuiviad como pintar o dibujar ',
    },
    'Regla 19': {
        'sintomas': 'no me gusta mi cuerpo, y con mis malas notas en los estudios siento que no sirvo para nada',
        'diagnostico': 'Inseguridad personal y problemas de autoconfianza',
        'recomendaciones': '\n1.Practica el journal\n2.Realiza cualquier tipo de actividad que te conecte con la naturaleza como el senderismo o jardineria\n3.Tomate un pequeño tiempo diario en el que puedasconectar contigo mim@s y de esta manera darte palabras de apoyo y de seguridad',
    },
    'Regla 20': {
        'sintomas': 'cada que que lo intento y fallo solo me culpo porque no me esforze por lograr lo que queria  ',
        'diagnostico': 'Miedo al fracaso (enfasis en clases )',
        'recomendaciones': '\n1. Establecer horarios equilibrados\n2.Pon un poco más de enfasis en los temas que no comprendes con tanta facilidad\n3.Pon en un una pequeña lista las actividades más importates y las que más tiempo rquieren',
    },
    'Regla 21': {
        'sintomas': 'no me siento a gusto contando mis problemas personas con terceros',
        'diagnostico': 'Dificultades para expresar emociones',
        'recomendaciones': '\n1.Realizas cartas sin enviar\n2.Recorta imágenes de revista y forma un pequeño collaje es una pequeña forma de expresr emociones complejas\n3.Meditaciónguiada y enofocada a las emociones',
    },
    'Regla 22': {
        'sintomas': 'se me difuclta separame de alguien como amigo,familiar o pareja solo no los puede dejar ir ',
        'diagnostico': 'Apego ansioso y emocional',
        'recomendaciones': '\n1. Empieza poco a poco a salir sol@ a la calle para tener más dependencia \n2. Si el apego es muy fuerte ve a terapias\n3.Practica la terapia de choque',
    },
    'Regla 23': {
        'sintomas': 'aveces solo me siento sin animos o desmotivado por todo y me aislo de las demas personas ',
        'diagnostico': 'Falta de conexión social',
        'recomendaciones': '\n1.Identifica a través de un mapa emocional el control de todas tus emociones\n2.Toma clases o talleres grupales donde puedas conectar con otras personas\n3.Entrena con n grupo de personas la comunicación acertiva',
    },
    'Regla 24': {
        'sintomas': 'me apego a las personas para no soltarlas y mas sin son amigos pareja o familiares para no estar sol@ ',
        'diagnostico': 'Apego emocional y miedo a la soledad', 
        'recomendaciones': '\n1.Reflexiona acerca de los limites emocionales\n2.Date una afirmación positiva diaria como: SOY SUFICIENTE POR MÍ MISMO\n3.invierte tu tiempo libre en actividades donde puedas desarrollar alguna de tus habilidades',
    },
    'Regla 25': {
        'sintomas': 'me da pena hablar con las personas porque me enredo y no se que decir ',
        'diagnostico': 'Dificultad para tomar la iniciativa en alguna conversación',
        'recomendaciones': '\n1.Realiza talleres de confianza para que así puedas soltarte más a la hora de hablar\n2.Toma lecturas sobre comunicación eficaz\n3.Crea una minilista de breves temas de conversación'
    },
    'Regla 26': {
        'sintomas': 'no me gusta experimentar porque no se que va a pasar',
        'diagnostico': 'Miedo a un cambio drastico en la vida o a perder algo del pasado',
        'recomendaciones': '\n1.Manten tu mente ocupada la gran parte de tu tiempo\n2.Carta de despedida al pasado donde expreses todos tus sentimientos con la mayor calridad posible\n3.Medita tu condiciones de vida y plantea la practica de soltar'
    },
    'Regla 27': {
        'sintomas': 'no puedo decir ni una palabra cuando quiero hablar con alguien nuevo o interactuar cona alguien más',
        'diagnostico': 'Miedo a las interaciones o al rechazo sociales',
        'recomendaciones': '\n1.Toma tu tiempo e inviertelo en actividades que refuercen tu autoconfianza\n2.Crea una pequeña lista con todas tus habilidades\n3.Escucha todas las mañana un podcats de autoayuda',
    },
    'Regla 28': {
        'sintomas': 'me gusta hacer las cosas sol@ sin ninguna ayuda de terceros',
        'diagnostico': 'Problemas de confianza',
        'recomendaciones': '\n1.Crea cartas al yo del futuro\n2.Realiza una lista de logros y fortalezas\n3.Ponte a diario un desfio personal',
    },
    'Regla 29': {
        'sintomas': 'necesito saber que mis familiares esten de acuerdo con lo que hago, y pienso',
        'diagnostico': 'Necesidad de adaptación por problemas de inseguridad personal',
        'recomendaciones': '\n1.Busca apoyo para que puedas comprender todo aquello que seas capaz de hacer\n2.Confia más en tus habilidades y destrezas para que puedas lograr ser autosuficiente sin importar lo que digan los demás\n3.Practica la meditación y lleva un control de tus pequeños o grandes logros diarios',

    },'Regla 30': {
        'sintomas': 'pensamientos contates al fracaso o a quedar solo',
        'diagnostico': 'Miedo a ser abandonado',
        'recomendaciones': '\n1. Buscar un grupo de apoyo o realizar terapia individual\n2.Practica la autocompasión\n3.Reconoer el apego para así poder soltarlo'
        
    },'Regla 31': {
        'sintomas': 'tengo que lograr ser perfecto en todo lo que le digo y hago',
        'diagnostico': 'Presón por cumplir con estandares muy elevados',
        'recomendaciones': '\n1. Establecer metas realistas \n2.Crear un mapa o lista de logras \n3.Fomenta más la autoexpresión a través de las actividades artísticas',
        
    },'Regla 32': {
        'sintomas': 'no me gusta mi físico ni como me veo   ',
        'diagnostico': 'Inseguridad sobre tu imagen',
        'recomendaciones': '\n1. Date a diario un grupo de frases de afirmaciones positivas\n2.Realiza una desintoxicaciones de las redes sociales\n3.Visualizate en grande en el futuro'
        
    },'Regla 33': {
        'sintomas': 'percepcion de sentirse confundido y desorientado',
        'diagnostico': 'Sensacion de desconexion de la realidad',
        'recomendaciones': '\n1.Manten la mente ocupada la gran mayoria del tiempo\n2. Distracción con reuniones de amigos\n3.Realiza rituales matutinos o nocturnos para lograr aclara el día y obtener una sensación de traquiliad',
        
    },'Regla 34': {
        'sintomas': 'no me gusta experimentar nada que no conozco',
        'diagnostico': 'Miedo o tomar riesgos',
        'recomendaciones': '\n1.Establece una lista de los riegos y clasificalos según el nivel de su nivel demanejabilidad\n2.Planteate un pequeño desafio semanal\n3.Hablar con amigos y familiares (más cercanos) para que así estas te puedan brindar su apoyo emocional'
        
    },'Regla 35': {
        'sintomas': 'estres academico y laboral',
        'diagnostico': 'reacciones defensivas ante el fracaso',
        'recomendaciones': '\n1. Tener una buena organizacón y establecer horarios\n2.Establecer metas más pequeñas\n3.Aplica ejercicios de respiración y relajación',
        
    },'Regla 36': {
        'sintomas': 'experimentar un nuevo estilo de vida',
        'diagnostico': 'Miedo a los cambios en la rutina',
        'recomendaciones': '\n1.Buscar apoyo de terceras personas en la cual le tengas confianza\n2.Planifica actividades proactivas\n3.Mantener un diario donde expreses como te sientes a diario',
        
    },'Regla 37': {
        'sintomas': 'debilidad con la aparencia fisica',
        'diagnostico': 'Problemas de autoaceptacion',
        'recomendaciones': '\n1. Confia más en ti y en todas tus capacidades\n2.Elabora una lista con todas tus habilidades\n3.Haz caso omiso a los comentarios de otras personas'
        
    },'Regla 38': {
        'sintomas': 'presión social y familiar',
        'diagnostico': 'Dificultates para establer metas',
        'recomendaciones': '\n1.Planteate a través de un pequeño mapa tus habilidades y destrezas\n2.Busca varias opciones y escoje la que mejor te venga\n3.Manten siempre una visualización de los resultados positivos ',
        
    },'Regla 39': {
        'sintomas': 'historia o traumas familiares  ',
        'diagnostico': 'Trastorno de ansiedad generalizada (TAG)',
        'recomendaciones': '\n1. Practicar ejercicios de ejercicios físico regular  como: Caminar, nada o correr\n2.Hacer relajación muscular progresiva\n3.Realiza actividades creativas que más sean de tu agrado',
        
    },'Regla 40': {
        'sintomas': 'se me suele ir la respiración y se me es dificil estar quiet@',
        'diagnostico': 'Ansiedad elevada',
        'recomendaciones': '\n1.Respirar profundamente para estar calmad@\n2.Practica la meditación guiada por un profesioanl\n3. Reliza ejercicios como caminar o trotar',        
    },'Regla 41': {
        'sintomas': 'por un momento no me siento con animos de nada, y luego de un  rato se empieza a pasar',
        'diagnostico': 'depresion tipo I',
        'recomendaciones': '\n1.Un entrenamiento suave de yoga\n2.caminata por las tardes al aire libre\n3.Aplicate e invierte más tiempo en tu cuidado personal',
        
    },'Regla 42': {
        'sintomas': 'me siento cansado, no duermo, ni como bien y lo unico que quiero estar solo',
        'diagnostico': 'Depresion tipo II',
        'recomendaciones': '\n1 Crear una rutina básica, pero que te mantenga gran parte del tiempo ocupad@ \n2.Llevar un diario personal\n3. Escuchar podcats relajantes o motivacionales',

    },'Regla 43': {
        'sintomas': 'ya no siento nada, solo un vacio, quisiera liberar este dolor solocon lagrimas',
        'diagnostico': 'Depresion tipo III',
        'recomendaciones': '\n1. Ejercicios aerobicos moderados\n2.Dedicate un tiempo de autocuidado\n3. Manten un horario de aliemnatción y de sueño regular',
   
    },'Regla 44': {
        'sintomas': 'me da nostalgia ver como otros lloran y se sienten mal',
        'diagnostico': 'Sensibilidad emocional',
        'recomendaciones': '\n1.Practica la tecnica de respiración profunda\n2. Escuchar música relajante como sonidos de la naturaleza\n3. Toma baños y mensajes relajantes',
    },
    'Regla 45': {
        'sintomas': 'no me puedo alejar de esa persona, ya que necesito de su aprovación ',
        'diagnostico': 'Dependencia de la validacion extrema',
        'recomendaciones': '\n1.Escribe afirmaciones diarias\n2. Tomate un tiempo para reflexionar sobre tus pequeños logros personales\n3. Realiza cartas de autcompasión hacia tí  mismo',
    },
    'Regla 46': {
        'sintomas': 'tengo un miedo constate de no poder montar nada en redes sociales por miedo a que me escriban cosas feas',
        'diagnostico': 'Efecto ciberacoso y necesidad de aceptación de tercero',
        'recomendaciones': '\n1. Tomar cursos de comunicación acertiva\n2. Establecer limites y aprender a decir NO \n3.Participa en grupo de apoyo para la autoestima',
    },
    'Regla 47': {
        'sintomas': 'no me puedo equivocar en nada, tengo que ser perfecto en todo lo que hago y digo',
        'diagnostico': 'Baja tolerancia a la fustracion',
        'recomendaciones': '\n1. Crea tu rpopio diario de emociones\n2.Busca una tecnica de reaolusión de problemas\n3. Establece metas a corto plazo',
    },
    'Regla 48': {
        'sintomas': 'quiero tener lo que esa persona tiene, lo que come, lo que hace o dice, porque lo hace sin errores o problemas',
        'diagnostico': 'Idealizacion exagerada de la vida de los demas',
        'recomendaciones': '\n1.Escrube una lista de afirmaciones sobre ti y repitelas diariamente\n2.Realizas proyevtos grupales o actividades comunitarias\n3. Toma cursos virtuales para reforzar alguna de tus habilidades',
    },
    'Regla 48': {
        'sintomas': 'todo lo que yo hago tiene que ser ordenado y estar de una manera adecuada para que de esta manera me pueda servir y gustar ',
        'diagnostico': 'Perfeccionismo',
        'recomendaciones': '\n1. Realiza tareas sin buscar la perfección\n2. Crea cuadros de arte abstracto\n3.Aprender a aceptar los errores',
    },
    'Regla 49': {
        'sintomas': 'no logro poder seguir el paso de las cosas y de las personas',
        'diagnostico': 'Falta de resilencia (resilencia, es el proceso para adaptarse bien a la adversidad)',
        'recomendaciones': '\n1.Analizar detalladamente el problema y su nivel degravedad\n2.Buscar redes o grupos de apoyo\n3. Establecer tus rutinas diarias',
    },
    'Regla 50': {
        'sintomas': 'cada cosa que hago lo hago mal sin importar nada',
        'diagnostico': 'Culpa intensiva',
        'recomendaciones': '\n1.Crea tu propia lista de responsabilidades\n2.Escribir afirmaciones positvas sobre ti mismo\n3.Aprender a identificar los limites personales',
    },
    'Regla 51': {
        'sintomas': 'me gusta  lo que hacen los demás y solo voy a mirar si a mi me funciona',
        'diagnostico': 'Identidad fragil',
        'recomendaciones': '\n1.Realiza actividades creativas como el artes plastics\n2. Ejercicios de compasión\n3.Probar nuevos roles',
    },
    'Regla 52': {
        'sintomas': 'me descontrolo y me comienzo sentir agitad@ ',
        'diagnostico': 'Reacciones desprorporcionadas',
        'recomendaciones': '\n1.Aplica una autoevaluación cognitiva\n2. Realiza la desconexión digital\n3.Crea rutinas de autocuidado personal',
    },
    'Regla 53': {
        'sintomas': 'la mejor étapa de mi vida es mi niñes es lo mejor que he vivido, quiero volver a ese tiempo otra vez',
        'diagnostico': 'Aferración a la infancia',
        'recomendaciones': '\n1.Invierte más tiempo de recreación con tus amigos\n2. Viajar y conocer lugares nuevos\n3.Realiza una carta de despedida al pasado, para que así lo puedas solat',
    },
    'Regla 54': {
        'sintomas': 'me interesa saber lo que losdemás dicen u opinan de mí ',
        'diagnostico': 'Dificultad para lidiar con la critica',
        'recomendaciones': '\n1.Escribe sobre ciertas experiencias\n2.Reflexiona sobre lo aprendido a través de la meditación\n3.Leer libros sobre el manejo emocional',
    },
    'Regla 55': {
        'sintomas': 'necesito ser llamad@ o que me digan de tal manera porque sino no me siento comod@',
        'diagnostico': 'Necedidad de ser etiquetado por inseguridades como el nombre',
        'recomendaciones': '\n1 Crea un diario de redescubrimiento\n2.Probar nombres alternativos\n3.Investiga la historia del nombre ',
    },
    'Regla 56': {
        'sintomas': 'mi estrato social y economico no me sirve para sali adelante con mi vida',
        'diagnostico': 'Inseguridad financiera',
        'recomendaciones': '\n1No darse por vencindo y todos los días levantarse con más ganas de salir adelante.\n2. No importa de donde vengas, si no a donde quieras llegar\n3.Lecura de libros y recursos en línea ',
    },
    'Regla 57': {
        'sintomas': 'me pierdo en mis pensamiento',
        'diagnostico': 'fuga de la realidad',
        'recomendaciones': '\n1.Reflexiones diarias\n2.Escribe cuentos animados, relatos o poemas\n3. Practica la danza o moviminetos libres',
    },
    'Regla 58': {
        'sintomas': 'dudo mucho de mi gran capacidad ',
        'diagnostico': 'Desconfianza en la intuision(decisiones)',
        'recomendaciones': '\n1. Leer libros sobre desarrollo personal\n2.Toma de pequeñas decisiones\n3. Visualización del futuro donde todo bien',
    },
    'Regla 59': {
        'sintomas': 'las opiniones de terceros hacia mi son importantes para mi autoestima',
        'diagnostico': 'Tendencia y dependencia a las critica',
        'recomendaciones': '\n1.Ejercicios de autoafirmación y aceptación personal\n2. Crear un mini diario de logros \n3.Buscar apoyo en amigos o familiares más cercanos ',
    },
    'Regla 60': {
        'sintomas': 'voy a evadir las peleas o discusiones porque no me gustan en mi vida ',
        'diagnostico': 'falta de habiliades para afrontar los problemas',
        'recomendaciones': '\n1. Realizar cursos de habilidades \n2. Videojuegos de resolución de problemas\n3. Identificación de los problemas comunes',
    },
    'Regla 61': {
        'sintomas': 'me apiao muy rápido de los problemas ajenos',
        'diagnostico': 'Autocompasión excesiva',
        'recomendaciones': '\n1.Aprender a identificar limites\n2.Practicar el NO \n3.Ponerte siempre como prioridad sin importar los demás',
    },
    'Regla 62': {
        'sintomas': 'miedo a perder una persona que tanto daño te hace y dependes emocionalmemte de él/ella',
        'diagnostico': 'Idealizacion de relacion toxica',
        'recomendaciones': '\n1.Asistir a talleres o conferencias sobre amor propio\n2.Busca terapia y trabaja la sanación emocional\n3.Aprender a identificar señales de advertencia',
    },
    'Regla 63': {
        'sintomas': 'queres que las personas te presten atención y querer hacer todo perfecto',
        'diagnostico': 'busqueda de aceptación constate ',
        'recomendaciones': '\n1.Aprender a comunicar necesidades de manera clara y respetuosa\n2.Probar nuevos hobbies\n3.Aprender a reconocer el apoyo',
    },
    'Regla 64': {
        'sintomas': 'pensar que las personas me hablan cada vez que quieren algo a cambio',
        'diagnostico': 'Aislamiento o sensación de desconexión emocional',
        'recomendaciones': '\n1. Participa enconcursos que te enseñen comunicación efectiva y acertiva\n2.Realia ejercicios de atención plena\n3.practica actividades al aire libre',
    },
    'Regla 65': {
        'sintomas': 'no me gusta que opinen de mi sobre mí sibre mi físico',
        'diagnostico': 'Aborrecimiento a la critica ',
        'recomendaciones': '\n1.Realiza ejercicios de autoevaluación\n2.Buscar terapia\n3.Practica la resiliencia'
    },
    'Regla 66': {
        'sintomas': 'mi mente se va y se dispersa de la realidad ',
        'diagnostico': 'Fugas mentales',
        'recomendaciones': '\n1.Realizar arte terapeutico\n2.Trabajar la escritura libre\n3.Pasar más tiempo con amigos o familiares',
    },
    'Regla 67': {
        'sintomas': 'querer estar sol@ y no saber nada de nadie',
        'diagnostico': 'Aislamiento automatico y mental',
        'recomendaciones': '\n1.Define una buena rutina estructurada\n2.Realiza actividades grupales pequeñas\n3.Invierte tu tiempo libre aprendiendo un nuevo idioma',
    },
    'Regla 68': {
        'sintomas': 'la gran mayoría de las personas me dan igual, y no me importa nada de ell@s',
        'diagnostico': 'Tendencia a generalizar',
        'recomendaciones': '\n1.Identificar las distorsiones mentales \n2.Desafiar los pensamientos negativos\n3.Analiza detalladamente la situación',
    },
    'Regla 69': {
        'sintomas': 'miedo constate a tener una relación ',
        'diagnostico': 'Dificultades para tener relaciones amorosas de pareja',
        'recomendaciones': '\n1.Realiza ejercicios de escuchar activiamente\n2.Aprender a tenerle paciecia a otro\n3. Aceptar tus errores para que puedan crecer juntos',
    },
    'Regla 70': {
        'sintomas': 'siempre dudo de las personas y no me parecen agradables',
        'diagnostico': 'Desconfiansa en los demas',
        'recomendaciones': '\n1.Tecnica de escuvha activa\n2.Fomentar la empatia\n3.Compartir tiempo de calidad con amigos más cercanos',
    },
    'Regla 71': {
        'sintomas': 'no me gusta que las cosas esten en otro lugar de donde las deje',
        'diagnostico': 'Orden excesivo',
        'recomendaciones': '\n1.Modificación de las rutinas diarias\n2.Practica danza improvisada\n3.Participa en reuniones o eventos donde el ambiente sea más relajado',
    },
    'Regla 72': {
        'sintomas': 'sensanción continua a senrir que todo lo malo solo me pasa a mi',
        'diagnostico': 'Tendencia a ser negativo',
        'recomendaciones': '\n1.Limitar el tiempo en las pantallas \n2.Dedicar tiempo a uno mismo\n3.Hacer voluntariado en comunidades vunerables',
    },
    'Regla 73': {
        'sintomas': 'dolor de cabeza constante por todo lo que suelo estuduiar',
        'diagnostico': 'Sobre carga de informacion',
        'recomendaciones': '\n1. Practica la meditacion\n2. Fija horarios y rutinas que se  acoplen a tu estilo de vida\n3.Haz una lista de tus actividades y realizalas en orden de importancia',
    },
    'Regla 74': {
        'sintomas': 'urgencia de decirle a las personas que basta y hasta ahi se puede llegar',
        'diagnostico': 'Necesidad de establecer limites',
        'recomendaciones': '\n1.Tomate un tiempoal día para analizar tus emociones\n2.Realizar viajes espontaneos\n3.Lecturas de libros sobre crecimiento personal',
    },
    'Regla 75': {
        'sintomas': 'cada vex que una persona dice algo sobre mi físico me afenta de manera significativa',
        'diagnostico': 'Hipersensibilidad a loscomentarios',
        'recomendaciones': '\n1.Reflexionar sobre comentarios positivos\n2.Identifica cada un de tus foirtalezas\n3.Toma cualquier curso para salir de tu zona de confort',
    },
    'Regla 76': {
        'sintomas': 'tener una mayor expresión con programas tecnologicos',
        'diagnostico': 'Dependencias de terapias digitales',
        'recomendaciones': '\n1.Buscar sesiones de terapias presenciales\n2.Practicar algun deporte en grupo\n3. Lecturas de libros en físico ',
    },
    'Regla 77': {
        'sintomas': 'no tener un tema de conversación agradable para  las demá personas',
        'diagnostico': 'Falta de habilidades interpersonales',
        'recomendaciones': '\n1.Participa en escenarios de resolusión de conflictos\n2.Asistir a talleres y concursos de oratoria\n3.Asistir a eventos comunitarios en los cuales también puedas participar',
    },
    'Regla 78': {
        'sintomas': 'sentimiento a identificarse con algun anime o caricatura',
        'diagnostico': 'Conexion emocional con personajes ficticios',
        'recomendaciones': '\n1.Apegarce más a la realidad \n2.Realiza taller de escrituras reflexivas \n3.Participa en creaciones teatrales',
    },
    'Regla 79': {
        'sintomas': 'necesidad constante de hacer las cosas bien ',
        'diagnostico': 'Intolerancia a la ambiguedad (ambiguedad, es lenguaje que puede entederse de varios modos o admitir interpretaciones)',
        'recomendaciones': '\n1.Participa en proyectos comunitarios\n2.Realiza juegos de mesas estratégicos\n3.Crea una rutina diaria donde puedas dar gratitud',
    },
    'Regla 80': {
        'sintomas': 'crear escenarios fasticos o irreales', 
        'diagnostico': 'Nostalgia por una inferencia idealizada',
        'recomendaciones': '\n1. Crear un proyecto de vida establenciendo metas claras\n2.Toma clases de improvisación para así desarrollar nuebps hobbies\n3.Lee novelas que se desarrollen con la época que estes idealizando',
    },
    'Regla 81': {
        'sintomas': 'difultad para consentrame en hacer tareas como domesticas u/o otras actividades del hogar',
        'diagnostico': 'Complejidad para establecer prioridades',
        'recomendaciones': '\n1.Liberar tiempo para enfocarse en otras tareas\n2.Participa constatntemente en talleres de regulación de tiempo \n3.Llevar un diario de gratitud donde registres todos tus logros',
    },
    'Regla 82': {
        'sintomas': 'sobrepensar las cosas y no encntar un sentido',
        'diagnostico': 'Exceso de reflexion',
        'recomendaciones': '\n1.Crear visualizaciones positivas\n2.Participa en la toma de decisiones rápidas\n2.Aceptar las imperfecciones\n3.Crea tu propia día sin tecnologia',
    },
    'Regla 83': {
        'sintomas': 'es mejor expresar mis emociones conmigo mism@ ',
        'diagnostico': 'Sentir un miedo constate a la vulnerabilidad ',
        'recomendaciones': '\n1.Realiza una lisgta de tus valores y creencias\n2.Empieza a tener pequeñas interacciones sociales\n3.Participa en actividades artística como de pintura',
    },
    'Regla 84': {
        'sintomas': 'miedo a expresar lo que me pasa a diario por miedo a ser juzgado',
        'diagnostico': 'sencasion de ser incomprendido',
        'recomendaciones': '\n1.Practica la acertividad\n2.Tomma meditación sobre la compasión\n3.Realiza ejercicios de retroalimentación',
    },
    'Regla 85': {
        'sintomas': 'el estres academico me hace volverme una persona amargada',
        'diagnostico': 'Perpercion negativa de la adultes',
        'recomendaciones': '\n1. Empieza a creae desafios mensauales\n2.Asistir a museos o teatros para aprovechar más el tiempo\n3.Organizar eventos y actividades recreativas',
    },
    'Regla 86': {
        'sintomas': 'tener un gusto por cosas que los demás pueden lograr ',
        'diagnostico': 'Tendencia a la comparacion costante',
        'recomendaciones': '\n1.Crea tu propio diario de reflexion personal\n2.Autoevaluate midiendo tus fortalezas\n3.Crear un plan de acción',
    },
    'Regla 87': {
        'sintomas': 'sentir que mi orientación sexual es un mal tema de conversación',
        'diagnostico': 'Incertudumbre sobre la identidad sexual o de genero',
        'recomendaciones': '\n1. Lectura sobre identidad de genero o sexual\n2.Conocer más a fondo las historias de las personas LGBTQ\n3. Asistir a eventos y participar como voluntariado',
    },
    'Regla 89': {
        'sintomas': 'sentirme mal por priorizarme a mi',
        'diagnostico': 'Culpa por priorizarme a mi mismo',
        'recomendaciones': '\n1.Dedicar unos minutos al día a la meditación y a la comprensión personal\n2.Ten reflexiones conciente contigo mism@\n3.Realiza a lectura delibros de desarrollo personal',
    },
    'Regla 90': {
        'sintomas': 'se me crea un vacio en la mente cuando quiero pensar ',
        'diagnostico': 'Tendencia a la paralisis por analizar',
        'recomendaciones': '\n1. Clasifica tus tareas segun la matriz de impotancia y urgencia\n2.Establecer metas claras\n3.Delegar decisiones menores',
    },
    'Regla 91': {
        'sintomas': 'sentir que mi familia tiene opinion de mi en cada momento que me ven ',
        'diagnostico': 'Difucltadad para mantener la critica familiar',
        'recomendaciones': '\n1. Reconocimiento emocional\n2.Perdonar a otros y a ti mismo \n3.Liberar el control de tus emociones',
    },
    'Regla 92': {
        'sintomas': 'me gusta hacer las cosas sol@ ',
        'diagnostico': 'Preferencia por el individualismo',
        'recomendaciones': '\n1.Dedicar tiempo a tus actividades personales\n2.Leer libros de crecimiento personal y etico\n3.Realiza viajes personales para conect7ar contigo mism@'
    },
    'Regla 93': {
        'sintomas': 'miedo a estar o sentirse sol@',
        'diagnostico': 'Dificultad para lidiar con la soledad o el abandono',
        'recomendaciones': '\n1.Solicita ayuda en un grupo de apoyo\n2. Adopción de una mascota \n3.Invierte tu tiempo aprendiendo algo nuevo',
    },
    'Regla 94': {
        'sintomas': 'tener todos los días que fijir estar bien emocionalmente',
        'diagnostico': 'Idealizacion  de la felicidad',
        'recomendaciones': '\n1.Terapia de aceptación y comprpmiso\n2.leer un libro referente a la filosofía\n3.Enfocarse en la meta y no en el camino',
    },
    'Regla 95': {
        'sintomas': 'todo los cometarios que digan de mi tiene que ser perfectos y sinceros',
        'diagnostico': 'Apego a la aprobacion',
        'recomendaciones': '\n1.Estudia tus capacidades sin importar lo que digan los demás\n2.Realizate una autoevaluación emocional\n3. Celebrar tus progresos por muy pequeños que sean',
    },
    'Regla 96': {
        'sintomas': 'sentir que los problemas se van cuando veo dibujo algo animado',
        'diagnostico': 'Fuga de la realidad a través de la ficción',
        'recomendaciones': '\n1.Practica la tecnica de escaneo corporal\n2.Crear un horario equilibrado \n3.Realiza una pausa entre vcada empisodio y capítulo',
    },
    'Regla 97': {
        'sintomas': 'me gusta divertirme, pero no molestando a los demás ',
        'diagnostico': 'Sensacion de culpa por diversion',
        'recomendaciones': '\n1.Realiza practicas de ejercicios alaire libre\n2.Disfruta de la vida permitiendote la acepyación \n3.Hablar con alguien para desahogrse',
    },
    'Regla 98': {
        'sintomas': 'nerviosismo por lo que pueda llegar a pasar ',
        'diagnostico': 'Tendencia a la sobre preocupacion',
        'recomendaciones': '\n1.Caminar o correr para despejar la mente\n2.Realiza artes y/o manualidades\n3.Practica la escritura',
    },
    'Regla 99': {
        'sintomas': 'todo mi físico siempre se tiene que ver bien',
        'diagnostico': 'Obsecion por imagen corporal',
        'recomendaciones': '\n1.Toma terapias de masajes \n2.lectu9ra sobre BODY POSITIVITY(lecturas sobre la aceptación del cuepo)\n3.Buscar ayuda de un asesoramiento nutricional',
    },
    'Regla 100': {
        'sintomas': 'sentimiento de tener que quedarme con esa persona porque es mi lugar seguro',
        'diagnostico': 'Apego emocional',
        'recomendaciones': '\n1.Participar en talleres que fomente la autoconfianza\n2.Establecer metas personales \n3.Realizar lecturas de libros sobre apego',
    },
    
    
    # Agrega más reglas según sea necesario...
}
def sistema_experto(sintomas):
    sintomas_normalizados = sintomas.strip().lower()
    
    resultados = []
    for regla in reglas.values():
        if regla['sintomas'] in sintomas_normalizados:
            resultados.append((regla['diagnostico'], regla['recomendaciones']))
    
    return resultados


def buscar_diagnostico():
    nombre = nombre_entry.get().strip()
    sintomas = sintomas_combobox.get().strip()  # Usamos el valor del combobox
    
    if not sintomas:
        result_text.set("Por favor, seleccione un síntoma.")
        return
    
    resultados = sistema_experto(sintomas)
    
    if resultados:
        resultados_text = [f"Resultados para {nombre}:\n"]
        for diag, recomendacion in resultados:
            resultados_text.append(f"Diagnóstico: {diag}\nRecomendaciones: {recomendacion}\n")
        result_text.set("\n".join(resultados_text))
    else:
        result_text.set(f"No se encontró una coincidencia para los síntomas ingresados de {nombre}.")
# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema Experto (IA) Camilo")

# Cambiar el color de fondo de la ventana
root.configure(bg='lightBlue1')

# Hacer que la ventana sea redimensionable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Ajustar el tamaño de la ventana automáticamente al contenido o mantener un tamaño inicial
root.geometry("800x600")


#funete de letra 
fuente_titulo = tkfont.Font(family='slant', size=16, weight='bold')
fuente_texto = tkfont.Font(family='family', size=12)

# Cargar y mostrar la imagen
try:
    img = PhotoImage(file='img\Sistema_copo.png')  # Ajusta la ruta según sea necesario
    img_label = tk.Label(root, image=img)
    img_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
except tk.TclError:
    print("No se pudo cargar la imagen. Asegúrate de que el archivo exista y esté en el formato correcto.")

# Etiqueta y barra de entrada para el nombre
tk.Label(root, text="Nombre:", bg='lightBlue1').grid(row=1, column=0, padx=10, pady=10)
nombre_entry = tk.Entry(root, width=50)
nombre_entry.grid(row=1, column=1, padx=10, pady=10)

sintomas = [regla['sintomas'] for regla in reglas.values() if regla['sintomas']]

# Etiqueta y barra desplegable para los síntomas
tk.Label(root, text="Síntomas (escribir o seleccionar):", bg='lightBlue1').grid(row=2, column=0, padx=11, pady=11)
sintomas_combobox = ttk.Combobox(root, values=sintomas, state='normal', width= 98)  # Cambia a 'normal' para permitir escritura
sintomas_combobox.grid(row=2, column=1, padx=11, pady=11)
sintomas_combobox.set("") 

# Botón para buscar diagnóstico
buscar_button = tk.Button(root, text="Buscar Diagnóstico", command=buscar_diagnostico)
buscar_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Área de texto para mostrar resultados
result_text = StringVar()
result_label = tk.Label(root, textvariable=result_text, justify='left', wraplength=400, bg='lightBlue1')
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()