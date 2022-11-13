# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
counter_attack = {"R": "P", "P": "S", "S": "R"} #siapin counter attack
steps = {} #rekam histori bermain lawan
def player(prev_play, opponent_history=[]):
	component = ['R', 'P', 'S'] #tentukan apa saja komponen bermainnya
  
	if prev_play in component:
		opponent_history.append(prev_play) #masukan rekaman bermain lawan ke memori unruk observasi
		
	n_obs = 6 #jumlah langkah sebelumnya dari lawan untuk diobservasi
	
	history = opponent_history
	
	guess = "R" #kalau data belum sampai n_obs maka tetapkan tebakan seperti ini
	
	if len(history) > n_obs:
		obs_pattern = join(history[-n_obs:]) #tentukan pattern observasi gabungkan beberapa langkah terakhir dari lawan, disini kita gunakan 6 langkah terakhir lawan
		
		if join(history[-(n_obs + 1):]) in steps.keys(): #cek apakah langkah lawan tsb ada di memori kita?
			steps[join(history[-(n_obs + 1):])] += 1 #kalau ada maka frekuensinya tambahkan 1
		else:
			steps[join(history[-(n_obs + 1):])] = 1 #kalau belum ada maka rekam lalu beri frekuensi 1
		
		options = [obs_pattern + "R", obs_pattern + "P", obs_pattern + "S"] #kemungkinan langkah berikutnya dari lawan
		
		for i in options: 
			if not i in steps.keys():
				steps[i] = 0 #apabila opsi diatas tidak ada maka masukkan ke memori dan beri nilai 0
		
		proba = max(options, key=lambda key: steps[key]) #dapatkan nilai tertinggi dari opsi dalam step
		
		guess = counter_attack[proba[-1]] #counter serangan lawan dengan nilai yg sudah kita tentukan diawal
		
	return guess

#buat fungsi untuk gabungkan step lawan dan untuk test fungsi diatas
def join(moves):
    return "".join(moves)
    play(player, quincy, 1000)
    play(player, mrugesh, 1000)
    play(player, abbey, 1000)
    play(player, kris, 1000)