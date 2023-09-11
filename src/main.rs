use std::path::Path;
use clap::{Parser, Subcommand};
use openssl::rand::rand_bytes;
use openssl::base64::encode_block;

const SECRET_VAULT: &str = ".secret_vault";

#[derive(Parser)]
#[command(author, version, about, long_about = None)]
#[command(propagate_version = true)]
struct Cli {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Subcommand)]
enum Commands {
    /// Adds a new entry
    Add { username: String, password: Option<String> },
    /// Deletes an entry
    Delete { username: String },

}

fn db_init() -> i32
{
    if Path::new(SECRET_VAULT).exists() {
        return 0;
    }

    let connection = sqlite::open(SECRET_VAULT).unwrap();
    let query = "CREATE TABLE passwords (username TEXT, password TEXT)";

    connection.execute(query).unwrap();
    return 0;
}

fn password_gen() -> [u8; 10]
{
    let mut buf = [0; 10];

    rand_bytes(&mut buf).unwrap();

    buf
}

fn add(username: &String, password: &Option<String>)
{
    let connection = sqlite::open(SECRET_VAULT).unwrap();

    let password = match password {
        None => {
            println!("a password is automatically generated for {username}");
            encode_block(&password_gen())
        },
        Some(_) => { (&password.as_deref().unwrap()).to_string() }
    };

    let query = format!("INSERT INTO passwords VALUES ('{username}', '{password}');");

    connection.execute(query).unwrap();

    println!("new username: {username} inserted successfully.");
}

fn delete(username: &String)
{
    println!("{username}");
}

fn main()
{
    let cli = Cli::parse();

    db_init();

    match &cli.command {
        Commands::Add { username, password } => {
            add(username, password);
        }
        Commands::Delete { username } => {
            delete(username);
        }
    }
}
